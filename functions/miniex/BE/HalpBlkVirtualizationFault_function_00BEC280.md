# HalpBlkVirtualizationFault

- RVA: `0x00BEC280`–`0x00BEC2F9` (길이 `121` bytes)
- VA: `0x0000000140BEC280`
- 실행 섹션: `MINIEX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFC50`
- 디코드: `28`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BEC2F3` → [HalpBlkFatalErrorHalt](HalpBlkFatalErrorHalt_function_00BEB900.md) (function, `0x00BEB900`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BEC280  48 83 EC 08                     sub rsp, 8
00BEC284  55                              push rbp
00BEC285  48 81 EC 58 01 00 00            sub rsp, 0x158
00BEC28C  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
00BEC294  C6 45 AB 01                     mov byte ptr [rbp - 0x55], 1
00BEC298  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00BEC29C  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00BEC2A0  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
00BEC2A4  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
00BEC2A8  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
00BEC2AC  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
00BEC2B0  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
00BEC2B4  FC                              cld
00BEC2B5  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
00BEC2B9  68 80 1F 00 00                  push 0x1f80
00BEC2BE  0F AE 14 24                     ldmxcsr dword ptr [rsp]
00BEC2C2  48 83 C4 08                     add rsp, 8
00BEC2C6  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
00BEC2CA  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
00BEC2CE  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
00BEC2D2  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
00BEC2D6  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
00BEC2DA  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
00BEC2DE  65 F0 48 FF 04 25 48 01 00 00   lock inc qword ptr gs:[0x148]
00BEC2E8  48 C7 C1 14 00 00 00            mov rcx, 0x14
00BEC2EF  48 8D 55 80                     lea rdx, [rbp - 0x80]
00BEC2F3  E8 08 F6 FF FF                  call 0x140beb900
00BEC2F8  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBlkVirtualizationFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned __int8 v_stack_m13D;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (8);
    v_rsp = (v_rsp) - (344);
    v_stack_m13D = 1;
    v_stack_m138 = result;
    v_stack_m130 = a1;
    v_stack_m128 = a2;
    v_stack_m120 = a3;
    v_stack_m118 = a4;
    v_stack_m110 = v_r10;
    v_stack_m108 = v_r11;
    v_rsp = (v_rsp) + (8);
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm2;
    v_stack_mC8 = v_xmm3;
    v_stack_mB8 = v_xmm4;
    v_stack_mA8 = v_xmm5;
    result = HalpBlkFatalErrorHalt(20, v_stack_m168, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpBlkVirtualizationFault(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint8_t v_stack_m13D;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (8);
    local_rsp = (local_rsp) - (344);
    v_stack_m13D = 1;
    v_stack_m138 = result;
    v_stack_m130 = Arg1;
    v_stack_m128 = Arg2;
    v_stack_m120 = Arg3;
    v_stack_m118 = Arg4;
    v_stack_m110 = local_r10;
    v_stack_m108 = local_r11;
    local_rsp = (local_rsp) + (8);
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm2;
    v_stack_mC8 = v_xmm3;
    v_stack_mB8 = v_xmm4;
    v_stack_mA8 = v_xmm5;
    result = HalpBlkFatalErrorHalt(20, v_stack_m168, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=miniex&rva=0x00BEC280&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BEC280[BB_00BEC280]
```
