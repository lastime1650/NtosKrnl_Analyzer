# TtmpUpdatePrimaryDisplayWnf

- RVA: `0x00776CEC`–`0x00776D77` (길이 `139` bytes)
- VA: `0x0000000140776CEC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDBA0`
- 디코드: `36`개 명령, `139/139` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00776D36` → [TtmpStartCallout](TtmpStartCallout_function_00776AA4.md) (function, `0x00776AA4`)
- `0x00776D60` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00776D6C` → [TtmpStopCallout](TtmpStopCallout_function_00776C24.md) (function, `0x00776C24`)

### Direct callers
- [TtmpPushTerminalDisplayStateOntoDevice](TtmpPushTerminalDisplayStateOntoDevice_function_00776838.md) at `0x007768C6`

### Static image references
- `0x00776D2B` → RVA `0x006B0D10` (`ZwUpdateWnfStateData`; read)
- `0x00776D49` → RVA `0x00020AE8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00776D60` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00776CEC  4C 8B DC                        mov r11, rsp
00776CEF  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
00776CF3  48 83 EC 78                     sub rsp, 0x78
00776CF7  83 7A 10 01                     cmp dword ptr [rdx + 0x10], 1
00776CFB  75 74                           jne 0x140776d71
00776CFD  8B 42 48                        mov eax, dword ptr [rdx + 0x48]
00776D00  A8 01                           test al, 1
00776D02  74 6D                           je 0x140776d71
00776D04  0F 57 C0                        xorps xmm0, xmm0
00776D07  45 89 43 B0                     mov dword ptr [r11 - 0x50], r8d
00776D0B  33 C0                           xor eax, eax
00776D0D  4C 8B C2                        mov r8, rdx
00776D10  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00776D15  48 8B D1                        mov rdx, rcx
00776D18  41 B9 06 00 00 00               mov r9d, 6
00776D1E  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00776D23  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00776D27  49 8D 4B C8                     lea rcx, [r11 - 0x38]
00776D2B  48 8D 05 DE 9F F3 FF            lea rax, [rip - 0xc6022]
00776D32  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
00776D36  E8 69 FD FF FF                  call 0x140776aa4
00776D3B  33 C0                           xor eax, eax
00776D3D  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00776D45  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00776D49  48 8D 0D 98 9D 8A FF            lea rcx, [rip - 0x756268]
00776D50  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00776D54  45 33 C9                        xor r9d, r9d
00776D57  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00776D5C  44 8D 40 04                     lea r8d, [rax + 4]
00776D60  E8 AB 9F F3 FF                  call 0x1406b0d10
00776D65  33 D2                           xor edx, edx
00776D67  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00776D6C  E8 B3 FE FF FF                  call 0x140776c24
00776D71  48 83 C4 78                     add rsp, 0x78
00776D75  C3                              ret
00776D76  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmpUpdatePrimaryDisplayWnf(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p18;

    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (120);
    if ((*(unsigned int *)(a2 + 16)) != 1) goto loc_00776D71;
    result = (unsigned int)(*(unsigned int *)(a2 + 72));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 72)))) & (1)) != 0) {
        *(unsigned int *)(v_rsp - 80) = a3;
        result = 0;
        a3 = a2;
        v_stack_m38 = v_xmm0;
        a2 = a1;
        a4 = 6;
        v_stack_m28 = v_xmm0;
        *(unsigned __int64 *)(v_rsp - 24) = 0;
        a1 = v_rsp - 56;
        result = v_rip - 811042;
        *(unsigned __int64 *)(v_rsp - 88) = result;
        result = TtmpStartCallout(a1, a2, a3, a4);
        result = 0;
        a2 = v_stack_p18;
        v_stack_m48 = 0;
        a1 = v_rip - 7692904;
        v_stack_m50 = 0;
        a4 = 0;
        v_stack_m58 = 0;
        a3 = result + 4;
        result = ZwUpdateWnfStateData(a1, a2, a3, a4);
        a2 = 0;
        a1 = v_stack_m38;
        result = TtmpStopCallout(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmpUpdatePrimaryDisplayWnf(int64_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p18;

    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (120);
    if ((*(uint32_t *)(arg2 + 0x10)) != 1) goto loc_00776D71;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x48));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) & (1)) != 0) {
        *(uint32_t *)(local_rsp - 0x50) = Arg3;
        result = 0;
        Arg3 = Arg2;
        v_stack_m38 = v_xmm0;
        Arg2 = Arg1;
        a4 = 6;
        v_stack_m28 = v_xmm0;
        *(uint64_t *)(local_rsp - 0x18) = 0;
        Arg1 = local_rsp - 56;
        result = v_rip - 811042;
        *(uint64_t *)(local_rsp - 0x58) = result;
        result = TtmpStartCallout(Arg1, Arg2, Arg3, a4);
        result = 0;
        Arg2 = v_stack_p18;
        v_stack_m48 = 0;
        Arg1 = v_rip - 7692904;
        v_stack_m50 = 0;
        a4 = 0;
        v_stack_m58 = 0;
        Arg3 = result + 4;
        result = ZwUpdateWnfStateData(Arg1, Arg2, Arg3, a4);
        Arg2 = 0;
        Arg1 = v_stack_m38;
        result = TtmpStopCallout(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (120);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x48` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00776CEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00776CEC[BB_00776CEC]
  bb_00776CFD[BB_00776CFD]
  bb_00776D04[BB_00776D04]
  bb_00776D71[BB_00776D71]
  bb_00776D76[BB_00776D76]
  bb_00776CEC -->|branch| bb_00776D71
  bb_00776CEC -->|fallthrough| bb_00776CFD
  bb_00776CFD -->|branch| bb_00776D71
  bb_00776CFD -->|fallthrough| bb_00776D04
  bb_00776D04 -->|flow| bb_00776D71
```
