# SeValidateImageData

- RVA: `0x0093ED98`–`0x0093EDD2` (길이 `58` bytes)
- VA: `0x000000014093ED98`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082E10`
- 디코드: `16`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0093EDC0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [MiValidateInPage](../../text/38/MiValidateInPage_function_00382E0C.md) at `0x003832A6`
- [MiValidateImagePfn](MiValidateImagePfn_function_0093EA08.md) at `0x0093EB8F`

### Static image references
- `0x0093ED9C` → RVA `0x00F04E68` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0093EDC0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0093ED98  48 83 EC 48                     sub rsp, 0x48
0093ED9C  48 8B 05 C5 60 5C 00            mov rax, qword ptr [rip + 0x5c60c5]
0093EDA3  4C 8B D1                        mov r10, rcx
0093EDA6  48 85 C0                        test rax, rax
0093EDA9  74 20                           je 0x14093edcb
0093EDAB  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0093EDB0  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0093EDB5  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
0093EDB9  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0093EDBD  49 8B CA                        mov rcx, r10
0093EDC0  E8 0B BD D7 FF                  call 0x1406baad0
0093EDC5  48 83 C4 48                     add rsp, 0x48
0093EDC9  C3                              ret
0093EDCA  CC                              int3
0093EDCB  B8 28 04 00 C0                  mov eax, 0xc0000428
0093EDD0  EB F3                           jmp 0x14093edc5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeValidateImageData(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if (*(unsigned __int64 *)(v_rip + 6054085) == 0) goto loc_0093EDCB;
    v_stack_m20 = a6;
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_0093EDC5:
    v_rsp = (v_rsp) + (72);
    return result;
loc_0093EDCB:
    goto loc_0093EDC5;
}
```

## 5. (Beta) C Style

```c
int64_t SeValidateImageData(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if (*(uint64_t *)(v_rip + 0x5C60C5) == 0) goto loc_0093EDCB;
    v_stack_m20 = Arg6;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
loc_0093EDC5:
    local_rsp = (local_rsp) + (72);
    return result;
loc_0093EDCB:
    goto loc_0093EDC5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0093ED98&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0093ED98[BB_0093ED98]
  bb_0093EDAB[BB_0093EDAB]
  bb_0093EDC5[BB_0093EDC5]
  bb_0093EDCA[BB_0093EDCA]
  bb_0093EDCB[BB_0093EDCB]
  bb_0093ED98 -->|branch| bb_0093EDCB
  bb_0093ED98 -->|fallthrough| bb_0093EDAB
  bb_0093EDAB -->|flow| bb_0093EDC5
  bb_0093EDCA -->|flow| bb_0093EDCB
  bb_0093EDCB -->|branch| bb_0093EDC5
```
