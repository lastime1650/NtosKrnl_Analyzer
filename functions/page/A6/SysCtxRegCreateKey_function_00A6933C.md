# SysCtxRegCreateKey

- RVA: `0x00A6933C`–`0x00A693AA` (길이 `110` bytes)
- VA: `0x0000000140A6933C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008EB20`
- 디코드: `28`개 명령, `110/110` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A69397` → [RegRtlCreateKeyTransacted](../93/RegRtlCreateKeyTransacted_function_0093207C.md) (function, `0x0093207C`)

### Direct callers
- [_PnpOpenPropertiesKey](../99/_PnpOpenPropertiesKey_function_009938A0.md) at `0x00993B47`
- [PnpCtxRegCreateKey](PnpCtxRegCreateKey_function_00A692E4.md) at `0x00A6932B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6933C  40 53                           push rbx
00A6933E  48 83 EC 50                     sub rsp, 0x50
00A69342  48 8B DA                        mov rbx, rdx
00A69345  45 8B D1                        mov r10d, r9d
00A69348  33 D2                           xor edx, edx
00A6934A  4D 8B D8                        mov r11, r8
00A6934D  48 85 C9                        test rcx, rcx
00A69350  74 51                           je 0x140a693a3
00A69352  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00A69356  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A6935B  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00A69363  45 8B C2                        mov r8d, r10d
00A69366  44 8B 8C 24 80 00 00 00         mov r9d, dword ptr [rsp + 0x80]
00A6936E  48 8B CB                        mov rcx, rbx
00A69371  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A69376  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00A6937E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A69383  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00A6938B  88 54 24 28                     mov byte ptr [rsp + 0x28], dl
00A6938F  49 8B D3                        mov rdx, r11
00A69392  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A69397  E8 E0 8C EC FF                  call 0x14093207c
00A6939C  48 83 C4 50                     add rsp, 0x50
00A693A0  5B                              pop rbx
00A693A1  C3                              ret
00A693A2  CC                              int3
00A693A3  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00A693A8  EB B1                           jmp 0x140a6935b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SysCtxRegCreateKey(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p40;

    v_rsp = (v_rsp) - (80);
    a2 = 0;
    if (a1 == 0) goto loc_00A693A3;
    v_stack_m18 = *(unsigned __int64 *)(a1 + 8);
loc_00A6935B:
    v_stack_m20 = a9;
    v_stack_m28 = a8;
    v_stack_m30 = 0;
    v_stack_m38 = a6;
    result = RegRtlCreateKeyTransacted(0, a3, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(a5));
    v_rsp = (v_rsp) + (80);
    return result;
loc_00A693A3:
    v_stack_p40 = a3;
    goto loc_00A6935B;
}
```

## 5. (Beta) C Style

```c
int64_t SysCtxRegCreateKey(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6, uint64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p40;

    local_rsp = (local_rsp) - (80);
    Arg2 = 0;
    if (Arg1 == 0) goto loc_00A693A3;
    v_stack_m18 = *(uint64_t *)(Arg1 + 0x8);
loc_00A6935B:
    v_stack_m20 = Arg9;
    v_stack_m28 = Arg8;
    v_stack_m30 = 0;
    v_stack_m38 = Arg6;
    result = RegRtlCreateKeyTransacted(0, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(Arg5));
    local_rsp = (local_rsp) + (80);
    return result;
loc_00A693A3:
    v_stack_p40 = Arg3;
    goto loc_00A6935B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6933C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A6933C[BB_00A6933C]
  bb_00A69352[BB_00A69352]
  bb_00A6935B[BB_00A6935B]
  bb_00A693A2[BB_00A693A2]
  bb_00A693A3[BB_00A693A3]
  bb_00A6933C -->|branch| bb_00A693A3
  bb_00A6933C -->|fallthrough| bb_00A69352
  bb_00A69352 -->|flow| bb_00A6935B
  bb_00A693A2 -->|flow| bb_00A693A3
  bb_00A693A3 -->|branch| bb_00A6935B
```
