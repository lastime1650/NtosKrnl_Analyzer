# RtlQueryImageFileExecutionOptions

- RVA: `0x0078B090`–`0x0078B107` (길이 `119` bytes)
- VA: `0x000000014078B090`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AE0FC`
- 디코드: `33`개 명령, `119/119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0078B0B3` → [RtlpOpenBaseImageFileOptionsKey](../A3/RtlpOpenBaseImageFileOptionsKey_function_00A3B9F4.md) (function, `0x00A3B9F4`)
- `0x0078B0DA` → [RtlQueryImageFileKeyOption](../A2/RtlQueryImageFileKeyOption_function_00A2D110.md) (function, `0x00A2D110`)
- `0x0078B0EF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [PsBootPhaseComplete](../77/PsBootPhaseComplete_function_0077EA18.md) at `0x0077EB14`
- [PsBootPhaseComplete](../77/PsBootPhaseComplete_function_0077EA18.md) at `0x0077EB47`
- [PsBootPhaseComplete](../77/PsBootPhaseComplete_function_0077EA18.md) at `0x0077EB5A`

### Static image references
- `0x0078B0DF` → RVA `0x00E67AF8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0078B0EF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0078B090  48 8B C4                        mov rax, rsp
0078B093  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0078B097  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0078B09B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0078B09F  57                              push rdi
0078B0A0  48 83 EC 30                     sub rsp, 0x30
0078B0A4  48 83 60 08 00                  and qword ptr [rax + 8], 0
0078B0A9  48 8D 48 08                     lea rcx, [rax + 8]
0078B0AD  49 8B F9                        mov rdi, r9
0078B0B0  48 8B F2                        mov rsi, rdx
0078B0B3  E8 3C 09 2B 00                  call 0x140a3b9f4
0078B0B8  8B D8                           mov ebx, eax
0078B0BA  85 C0                           test eax, eax
0078B0BC  78 36                           js 0x14078b0f4
0078B0BE  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0078B0C4  41 B8 04 00 00 00               mov r8d, 4
0078B0CA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0078B0CF  4C 8B CF                        mov r9, rdi
0078B0D2  48 8B D6                        mov rdx, rsi
0078B0D5  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
0078B0DA  E8 31 20 2A 00                  call 0x140a2d110
0078B0DF  83 3D 12 CA 6D 00 00            cmp dword ptr [rip + 0x6dca12], 0
0078B0E6  8B D8                           mov ebx, eax
0078B0E8  74 0A                           je 0x14078b0f4
0078B0EA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0078B0EF  E8 BC 21 F2 FF                  call 0x1406ad2b0
0078B0F4  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0078B0F9  8B C3                           mov eax, ebx
0078B0FB  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0078B100  48 83 C4 30                     add rsp, 0x30
0078B104  5F                              pop rdi
0078B105  C3                              ret
0078B106  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlQueryImageFileExecutionOptions(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (48);
    result = RtlpOpenBaseImageFileOptionsKey(v_rsp + 8, a2, a3, a4);
    if (sign_flag) goto loc_0078B0F4;
    v_stack_m18 = 4;
    result = RtlQueryImageFileKeyOption(v_stack_p8, a2, 4, a4);
    if ((*(unsigned int *)(v_rip + 7195154)) != 0) {
        a1 = v_stack_p8;
        result = ZwClose(a1, a2, 4, a4);
    }
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t RtlQueryImageFileExecutionOptions(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (48);
    result = RtlpOpenBaseImageFileOptionsKey(local_rsp + 8, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0078B0F4;
    v_stack_m18 = 4;
    result = RtlQueryImageFileKeyOption(v_stack_p8, Arg2, 4, Arg4);
    if ((*(uint32_t *)(v_rip + 0x6DCA12)) != 0) {
        Arg1 = v_stack_p8;
        result = ZwClose(Arg1, Arg2, 4, Arg4);
    }
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0078B090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0078B090[BB_0078B090]
  bb_0078B0BE[BB_0078B0BE]
  bb_0078B0EA[BB_0078B0EA]
  bb_0078B0F4[BB_0078B0F4]
  bb_0078B106[BB_0078B106]
  bb_0078B090 -->|branch| bb_0078B0F4
  bb_0078B090 -->|fallthrough| bb_0078B0BE
  bb_0078B0BE -->|branch| bb_0078B0F4
  bb_0078B0BE -->|fallthrough| bb_0078B0EA
  bb_0078B0EA -->|flow| bb_0078B0F4
```
