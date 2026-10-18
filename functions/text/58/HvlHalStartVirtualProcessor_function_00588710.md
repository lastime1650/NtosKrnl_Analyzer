# HvlHalStartVirtualProcessor

- RVA: `0x00588710`–`0x0058872F` (길이 `31` bytes)
- VA: `0x0000000140588710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0058871D` → [VslStartSecureProcessor](../../page/71/VslStartSecureProcessor_function_00719714.md) (function, `0x00719714`)
- `0x00588724` → [HvlpStartVirtualProcessor](HvlpStartVirtualProcessor_function_00586ADC.md) (function, `0x00586ADC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00588714` → RVA `0x00FC6A84` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0058871D` → [VslStartSecureProcessor](../../page/71/VslStartSecureProcessor_function_00719714.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00588710  48 83 EC 28                     sub rsp, 0x28
00588714  80 3D 69 E3 A3 00 00            cmp byte ptr [rip + 0xa3e369], 0
0058871B  74 07                           je 0x140588724
0058871D  E8 F2 0F 19 00                  call 0x140719714
00588722  EB 05                           jmp 0x140588729
00588724  E8 B3 E3 FF FF                  call 0x140586adc
00588729  48 83 C4 28                     add rsp, 0x28
0058872D  C3                              ret
0058872E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlHalStartVirtualProcessor(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 10740585)) == 0) goto loc_00588724;
    result = VslStartSecureProcessor(a1, a2, a3, a4);
    goto loc_00588729;
loc_00588724:
    result = HvlpStartVirtualProcessor(a1, a2, a3, a4);
loc_00588729:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HvlHalStartVirtualProcessor(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0xA3E369)) == 0) goto loc_00588724;
    result = VslStartSecureProcessor(a1, a2, a3, a4);
    goto loc_00588729;
loc_00588724:
    result = HvlpStartVirtualProcessor(a1, a2, a3, a4);
loc_00588729:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00588710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00588710[BB_00588710]
  bb_0058871D[BB_0058871D]
  bb_00588724[BB_00588724]
  bb_00588729[BB_00588729]
  bb_0058872E[BB_0058872E]
  bb_00588710 -->|branch| bb_00588724
  bb_00588710 -->|fallthrough| bb_0058871D
  bb_0058871D -->|branch| bb_00588729
  bb_00588724 -->|flow| bb_00588729
```
