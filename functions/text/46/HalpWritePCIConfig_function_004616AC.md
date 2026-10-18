# HalpWritePCIConfig

- RVA: `0x004616AC`–`0x00461725` (길이 `121` bytes)
- VA: `0x00000001404616AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9EA8`
- 디코드: `35`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004616D1` → [HalpValidPCISlot](HalpValidPCISlot_function_00461A08.md) (function, `0x00461A08`)
- `0x004616FE` → [HalpPCIConfig](../23/HalpPCIConfig_function_00235980.md) (function, `0x00235980`)

### Direct callers
- [HalpSetPCIData](HalpSetPCIData_function_004615B4.md) at `0x00461654`
- [HalpValidPCISlot](HalpValidPCISlot_function_00461A08.md) at `0x00461AC2`
- [sub_006F25EC](../6F/Unknown_function_006F25EC.md) at `0x006F265D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004616AC  48 8B C4                        mov rax, rsp
004616AF  48 89 58 08                     mov qword ptr [rax + 8], rbx
004616B3  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
004616B7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
004616BB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
004616BF  41 56                           push r14
004616C1  48 83 EC 40                     sub rsp, 0x40
004616C5  4D 8B F1                        mov r14, r9
004616C8  41 8B D8                        mov ebx, r8d
004616CB  40 8A F2                        mov sil, dl
004616CE  0F B7 E9                        movzx ebp, cx
004616D1  E8 32 03 00 00                  call 0x140461a08
004616D6  84 C0                           test al, al
004616D8  74 47                           je 0x140461721
004616DA  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
004616DE  4D 8B CE                        mov r9, r14
004616E1  8B 7C 24 78                     mov edi, dword ptr [rsp + 0x78]
004616E5  44 8B C3                        mov r8d, ebx
004616E8  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
004616F0  40 8A D6                        mov dl, sil
004616F3  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
004616F7  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
004616FB  0F B7 CD                        movzx ecx, bp
004616FE  E8 7D 42 DD FF                  call 0x140235980
00461703  8B C7                           mov eax, edi
00461705  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0046170A  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0046170F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00461714  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00461719  48 83 C4 40                     add rsp, 0x40
0046171D  41 5E                           pop r14
0046171F  C3                              ret
00461720  CC                              int3
00461721  33 C0                           xor eax, eax
00461723  EB E0                           jmp 0x140461705
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpWritePCIConfig(unsigned __int16 a1, unsigned __int8 a2, int a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = HalpValidPCISlot(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00461721;
    v_stack_m18 = 1;
    v_stack_m20 = (unsigned int)((unsigned int)(a6));
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = HalpPCIConfig(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
loc_00461705:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)(a6)));
loc_00461721:
    result = 0;
    goto loc_00461705;
}
```

## 5. (Beta) C Style

```c
int64_t HalpWritePCIConfig(uint16_t Arg1, uint8_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = HalpValidPCISlot(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00461721;
    v_stack_m18 = 1;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = HalpPCIConfig(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
loc_00461705:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)(Arg6)));
loc_00461721:
    result = 0;
    goto loc_00461705;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004616AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004616AC[BB_004616AC]
  bb_004616DA[BB_004616DA]
  bb_00461705[BB_00461705]
  bb_00461720[BB_00461720]
  bb_00461721[BB_00461721]
  bb_004616AC -->|branch| bb_00461721
  bb_004616AC -->|fallthrough| bb_004616DA
  bb_004616DA -->|flow| bb_00461705
  bb_00461720 -->|flow| bb_00461721
  bb_00461721 -->|branch| bb_00461705
```
