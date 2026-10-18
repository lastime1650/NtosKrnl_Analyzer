# SepLengthSidAndAttributesArray

- RVA: `0x009C9CB8`–`0x009C9D60` (길이 `168` bytes)
- VA: `0x00000001409C9CB8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0A7C`
- 디코드: `49`개 명령, `168/168` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009C9CEA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009C9D21` → [SeCaptureSidAndAttributesArray](SeCaptureSidAndAttributesArray_function_009C9D70.md) (function, `0x009C9D70`)
- `0x009C9D3C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SeSetTokenTamperProtection](../../text/60/SeSetTokenTamperProtection_function_00609644.md) at `0x006098AC`
- [SepSetTokenCapabilities](SepSetTokenCapabilities_function_009C9AF4.md) at `0x009C9B55`
- [sub_00B3F630](../B3/Unknown_function_00B3F630.md) at `0x00B3F6E4`
- [sub_00B412E4](../B4/Unknown_function_00B412E4.md) at `0x00B41321`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009C9CEA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009C9D3C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C9CB8  48 8B C4                        mov rax, rsp
009C9CBB  48 89 58 08                     mov qword ptr [rax + 8], rbx
009C9CBF  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
009C9CC3  56                              push rsi
009C9CC4  57                              push rdi
009C9CC5  41 56                           push r14
009C9CC7  48 83 EC 60                     sub rsp, 0x60
009C9CCB  33 DB                           xor ebx, ebx
009C9CCD  49 8B F0                        mov rsi, r8
009C9CD0  8B EA                           mov ebp, edx
009C9CD2  89 58 20                        mov dword ptr [rax + 0x20], ebx
009C9CD5  4C 8B F1                        mov r14, rcx
009C9CD8  48 89 58 D8                     mov qword ptr [rax - 0x28], rbx
009C9CDC  B9 00 01 00 00                  mov ecx, 0x100
009C9CE1  41 B8 53 65 53 61               mov r8d, 0x61536553
009C9CE7  8D 53 08                        lea edx, [rbx + 8]
009C9CEA  E8 01 84 1B 00                  call 0x140b820f0
009C9CEF  48 8B F8                        mov rdi, rax
009C9CF2  48 85 C0                        test rax, rax
009C9CF5  74 62                           je 0x1409c9d59
009C9CF7  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
009C9CFF  4C 8B CF                        mov r9, rdi
009C9D02  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009C9D07  45 33 C0                        xor r8d, r8d
009C9D0A  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009C9D0F  8B D5                           mov edx, ebp
009C9D11  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C9D16  49 8B CE                        mov rcx, r14
009C9D19  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
009C9D21  E8 4A 00 00 00                  call 0x1409c9d70
009C9D26  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
009C9D2D  3D 23 00 00 C0                  cmp eax, 0xc0000023
009C9D32  89 0E                           mov dword ptr [rsi], ecx
009C9D34  48 8B CF                        mov rcx, rdi
009C9D37  0F 45 D8                        cmovne ebx, eax
009C9D3A  33 D2                           xor edx, edx
009C9D3C  E8 2F 8B 1B 00                  call 0x140b82870
009C9D41  8B C3                           mov eax, ebx
009C9D43  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
009C9D48  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
009C9D4C  49 8B 6B 28                     mov rbp, qword ptr [r11 + 0x28]
009C9D50  49 8B E3                        mov rsp, r11
009C9D53  41 5E                           pop r14
009C9D55  5F                              pop rdi
009C9D56  5E                              pop rsi
009C9D57  C3                              ret
009C9D58  CC                              int3
009C9D59  B8 9A 00 00 C0                  mov eax, 0xc000009a
009C9D5E  EB E3                           jmp 0x1409c9d43
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepLengthSidAndAttributesArray(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    v_rsp = (v_rsp) - (96);
    v_rbx = 0;
    *(unsigned int *)(v_rsp + 32) = 0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = ExAllocatePool2(256, v_rbx + 8, (unsigned int)(0x61536553ULL), a4);
    if (result == 0) goto loc_009C9D59;
    v_stack_m38 = v_stack_p20;
    a3 = 0;
    v_stack_m40 = v_stack_m28;
    v_stack_m58 = 8;
    result = SeCaptureSidAndAttributesArray(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, result);
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(v_stack_p20));
    if (((unsigned int)(result)) != 0xC0000023ULL) { v_rbx = (unsigned int)(result); }
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, result);
loc_009C9D43:
    return (unsigned int)((unsigned int)(v_rbx));
loc_009C9D59:
    goto loc_009C9D43;
}
```

## 5. (Beta) C Style

```c
int64_t SepLengthSidAndAttributesArray(int64_t Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m58;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    local_rsp = (local_rsp) - (96);
    local_rbx = 0;
    *(uint32_t *)(local_rsp + 0x20) = 0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = ExAllocatePool2(256, local_rbx + 8, (uint32_t)(0x61536553ULL), a4);
    if (result == 0) goto loc_009C9D59;
    v_stack_m38 = v_stack_p20;
    Arg3 = 0;
    v_stack_m40 = v_stack_m28;
    v_stack_m58 = 8;
    result = SeCaptureSidAndAttributesArray(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, result);
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(v_stack_p20));
    if (((uint32_t)(result)) != 0xC0000023ULL) { local_rbx = (uint32_t)(result); }
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, result);
loc_009C9D43:
    return (uint32_t)((uint32_t)(local_rbx));
loc_009C9D59:
    goto loc_009C9D43;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C9CB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009C9CB8[BB_009C9CB8]
  bb_009C9CF7[BB_009C9CF7]
  bb_009C9D43[BB_009C9D43]
  bb_009C9D58[BB_009C9D58]
  bb_009C9D59[BB_009C9D59]
  bb_009C9CB8 -->|branch| bb_009C9D59
  bb_009C9CB8 -->|fallthrough| bb_009C9CF7
  bb_009C9CF7 -->|flow| bb_009C9D43
  bb_009C9D58 -->|flow| bb_009C9D59
  bb_009C9D59 -->|branch| bb_009C9D43
```
