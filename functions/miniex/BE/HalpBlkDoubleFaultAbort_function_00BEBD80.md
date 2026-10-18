# HalpBlkDoubleFaultAbort

- RVA: `0x00BEBD80`–`0x00BEBDF5` (길이 `117` bytes)
- VA: `0x0000000140BEBD80`
- 실행 섹션: `MINIEX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFBB0`
- 디코드: `27`개 명령, `117/117` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BEBDEF` → [HalpBlkFatalErrorHalt](HalpBlkFatalErrorHalt_function_00BEB900.md) (function, `0x00BEB900`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BEBD80  55                              push rbp
00BEBD81  48 81 EC 58 01 00 00            sub rsp, 0x158
00BEBD88  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
00BEBD90  C6 45 AB 01                     mov byte ptr [rbp - 0x55], 1
00BEBD94  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00BEBD98  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00BEBD9C  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
00BEBDA0  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
00BEBDA4  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
00BEBDA8  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
00BEBDAC  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
00BEBDB0  FC                              cld
00BEBDB1  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
00BEBDB5  68 80 1F 00 00                  push 0x1f80
00BEBDBA  0F AE 14 24                     ldmxcsr dword ptr [rsp]
00BEBDBE  48 83 C4 08                     add rsp, 8
00BEBDC2  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
00BEBDC6  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
00BEBDCA  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
00BEBDCE  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
00BEBDD2  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
00BEBDD6  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
00BEBDDA  65 F0 48 FF 04 25 E8 00 00 00   lock inc qword ptr gs:[0xe8]
00BEBDE4  48 C7 C1 08 00 00 00            mov rcx, 8
00BEBDEB  48 8D 55 80                     lea rdx, [rbp - 0x80]
00BEBDEF  E8 0C FB FF FF                  call 0x140beb900
00BEBDF4  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBlkDoubleFaultAbort(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned __int8 v_stack_m135;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;

    v_rsp = (v_rsp) - (344);
    v_stack_m135 = 1;
    v_stack_m130 = result;
    v_stack_m128 = a1;
    v_stack_m120 = a2;
    v_stack_m118 = a3;
    v_stack_m110 = a4;
    v_stack_m108 = v_r10;
    v_stack_m100 = v_r11;
    v_rsp = (v_rsp) + (8);
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    v_stack_mD0 = v_xmm2;
    v_stack_mC0 = v_xmm3;
    v_stack_mB0 = v_xmm4;
    v_stack_mA0 = v_xmm5;
    result = HalpBlkFatalErrorHalt(8, v_stack_m160, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpBlkDoubleFaultAbort(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint8_t v_stack_m135;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;

    local_rsp = (local_rsp) - (344);
    v_stack_m135 = 1;
    v_stack_m130 = result;
    v_stack_m128 = Arg1;
    v_stack_m120 = Arg2;
    v_stack_m118 = Arg3;
    v_stack_m110 = Arg4;
    v_stack_m108 = local_r10;
    v_stack_m100 = local_r11;
    local_rsp = (local_rsp) + (8);
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    v_stack_mD0 = v_xmm2;
    v_stack_mC0 = v_xmm3;
    v_stack_mB0 = v_xmm4;
    v_stack_mA0 = v_xmm5;
    result = HalpBlkFatalErrorHalt(8, v_stack_m160, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=miniex&rva=0x00BEBD80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BEBD80[BB_00BEBD80]
```
