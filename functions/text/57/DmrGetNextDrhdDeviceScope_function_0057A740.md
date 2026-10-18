# DmrGetNextDrhdDeviceScope

- RVA: `0x0057A740`–`0x0057A766` (길이 `38` bytes)
- VA: `0x000000014057A740`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0057A75B` → [DmrGetNextDeviceScope](DmrGetNextDeviceScope_function_0057AA30.md) (function, `0x0057AA30`)

### Direct callers
- [HalpIvtLegacyProcessDrhdEntry](HalpIvtLegacyProcessDrhdEntry_function_00578C58.md) at `0x00579043`
- [HalpIvtProcessDrhdEntry](HalpIvtProcessDrhdEntry_function_005794B4.md) at `0x005798AB`
- [DmrFindDrhdForDeviceScope](DmrFindDrhdForDeviceScope_function_0057A6A0.md) at `0x0057A6F0`
- [DmrValidateDeviceScope](DmrValidateDeviceScope_function_0057AACC.md) at `0x0057AB05`
- [DmrValidateDeviceScope](DmrValidateDeviceScope_function_0057AACC.md) at `0x0057AB76`
- [DmrValidateDeviceScope](DmrValidateDeviceScope_function_0057AACC.md) at `0x0057AB88`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057A740  48 83 EC 28                     sub rsp, 0x28
0057A744  4C 8B C2                        mov r8, rdx
0057A747  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
0057A74B  48 03 D1                        add rdx, rcx
0057A74E  48 3B D1                        cmp rdx, rcx
0057A751  77 04                           ja 0x14057a757
0057A753  33 C0                           xor eax, eax
0057A755  EB 09                           jmp 0x14057a760
0057A757  48 83 C1 10                     add rcx, 0x10
0057A75B  E8 D0 02 00 00                  call 0x14057aa30
0057A760  48 83 C4 28                     add rsp, 0x28
0057A764  C3                              ret
0057A765  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DmrGetNextDrhdDeviceScope(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (*(unsigned __int16 *)(a1 + 2)) + (a1);
    if (a2 > a1) goto loc_0057A757;
    result = 0;
    goto loc_0057A760;
loc_0057A757:
    a1 = (a1) + (16);
    result = DmrGetNextDeviceScope(a1, a2, a2, a4);
loc_0057A760:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DmrGetNextDrhdDeviceScope(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = (*(uint16_t *)(arg1 + 0x2)) + (Arg1);
    if (Arg2 > Arg1) goto loc_0057A757;
    result = 0;
    goto loc_0057A760;
loc_0057A757:
    Arg1 = (Arg1) + (16);
    result = DmrGetNextDeviceScope(Arg1, Arg2, Arg2, a4);
loc_0057A760:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057A740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057A740[BB_0057A740]
  bb_0057A753[BB_0057A753]
  bb_0057A757[BB_0057A757]
  bb_0057A760[BB_0057A760]
  bb_0057A765[BB_0057A765]
  bb_0057A740 -->|branch| bb_0057A757
  bb_0057A740 -->|fallthrough| bb_0057A753
  bb_0057A753 -->|branch| bb_0057A760
  bb_0057A757 -->|flow| bb_0057A760
```
