# NtCreateSection

- RVA: `0x008AA3D0`–`0x008AA479` (길이 `169` bytes)
- VA: `0x00000001408AA3D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F60C`
- 디코드: `38`개 명령, `169/169` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008AA440` → [MiCreateSectionCommon](MiCreateSectionCommon_function_008A9AA4.md) (function, `0x008A9AA4`)

### Direct callers
- [DifNtCreateSectionWrapper](../../text/63/DifNtCreateSectionWrapper_function_00637460.md) at `0x0063757F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008AA3D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008AA3D5  57                              push rdi
008AA3D6  48 83 EC 70                     sub rsp, 0x70
008AA3DA  44 8B 94 24 A8 00 00 00         mov r10d, dword ptr [rsp + 0xa8]
008AA3E2  45 33 DB                        xor r11d, r11d
008AA3E5  41 8B C2                        mov eax, r10d
008AA3E8  0F 57 C0                        xorps xmm0, xmm0
008AA3EB  48 8B F9                        mov rdi, rcx
008AA3EE  41 8B DB                        mov ebx, r11d
008AA3F1  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
008AA3F6  83 E0 7F                        and eax, 0x7f
008AA3F9  75 59                           jne 0x1408aa454
008AA3FB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AA404  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
008AA40A  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008AA412  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
008AA416  48 8B CF                        mov rcx, rdi
008AA419  C7 44 24 48 01 00 00 00         mov dword ptr [rsp + 0x48], 1
008AA421  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
008AA426  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
008AA42B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008AA430  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
008AA437  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
008AA43C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008AA440  E8 5F F6 FF FF                  call 0x1408a9aa4
008AA445  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
008AA44D  48 83 C4 70                     add rsp, 0x70
008AA451  5F                              pop rdi
008AA452  C3                              ret
008AA453  CC                              int3
008AA454  41 83 E2 80                     and r10d, 0xffffff80
008AA458  44 89 5C 24 6C                  mov dword ptr [rsp + 0x6c], r11d
008AA45D  FF C8                           dec eax
008AA45F  48 C7 44 24 60 02 00 00 00      mov qword ptr [rsp + 0x60], 2
008AA468  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
008AA46C  48 8D 5C 24 60                  lea rbx, [rsp + 0x60]
008AA471  41 BB 01 00 00 00               mov r11d, 1
008AA477  EB 82                           jmp 0x1408aa3fb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCreateSection(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int8 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (112);
    v_r11 = 0;
    v_stack_m18 = v_xmm0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (127));
    if (condition_is_not_equal) goto loc_008AA454;
loc_008AA3FB:
    v_stack_m28 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m30 = 1;
    v_stack_m38 = 0;
    v_stack_m40 = 0;
    v_stack_m48 = a7;
    v_stack_m50 = (unsigned int)((unsigned int)(a6));
    v_stack_m58 = (unsigned int)((unsigned int)(a5));
    result = MiCreateSectionCommon(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
loc_008AA454:
    v_r10 = (unsigned int)(((unsigned int)(a6)) & (0xFFFFFF80ULL));
    v_stack_p6C = 0;
    result = (unsigned int)((result) - 1);
    v_stack_p60 = 2;
    v_stack_p68 = (unsigned int)(result);
    goto loc_008AA3FB;
}
```

## 5. (Beta) C Style

```c
int64_t NtCreateSection(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint8_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (112);
    local_r11 = 0;
    v_stack_m18 = v_xmm0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (127));
    if (condition_is_not_equal) goto loc_008AA454;
loc_008AA3FB:
    v_stack_m28 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m30 = 1;
    v_stack_m38 = 0;
    v_stack_m40 = 0;
    v_stack_m48 = Arg7;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m58 = (uint32_t)((uint32_t)(Arg5));
    result = MiCreateSectionCommon(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (112);
    return result;
loc_008AA454:
    local_r10 = (uint32_t)(((uint32_t)(Arg6)) & (0xFFFFFF80ULL));
    v_stack_p6C = 0;
    result = (uint32_t)((result) - 1);
    v_stack_p60 = 2;
    v_stack_p68 = (uint32_t)(result);
    goto loc_008AA3FB;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AA3D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008AA3D0[BB_008AA3D0]
  bb_008AA3FB[BB_008AA3FB]
  bb_008AA453[BB_008AA453]
  bb_008AA454[BB_008AA454]
  bb_008AA3D0 -->|branch| bb_008AA454
  bb_008AA3D0 -->|fallthrough| bb_008AA3FB
  bb_008AA453 -->|flow| bb_008AA454
  bb_008AA454 -->|branch| bb_008AA3FB
```
