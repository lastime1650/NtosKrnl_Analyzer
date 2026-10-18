# HalpInitNonBusHandler

- RVA: `0x00C1E320`–`0x00C1E34C` (길이 `44` bytes)
- VA: `0x0000000140C1E320`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpPciInitSystem](../../pagelk/B5/HalpPciInitSystem_function_00B5D6C0.md) at `0x00B5D6E5`

### Static image references
- `0x00C1E320` → RVA `0x0046C390` (`HalpTranslateBusAddress`; read)
- `0x00C1E327` → RVA `0x00E00828` (`.data`; write)
- `0x00C1E32E` → RVA `0x00A84330` (`ArbAddReserved`; read)
- `0x00C1E335` → RVA `0x00E00830` (`.data`; write)
- `0x00C1E33C` → RVA `0x0053F2E0` (`HalpFindBusAddressTranslation`; read)
- `0x00C1E343` → RVA `0x00E00840` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1E320  48 8D 05 69 E0 84 FF            lea rax, [rip - 0x7b1f97]
00C1E327  48 89 05 FA 24 1E 00            mov qword ptr [rip + 0x1e24fa], rax
00C1E32E  48 8D 05 FB 5F E6 FF            lea rax, [rip - 0x19a005]
00C1E335  48 89 05 F4 24 1E 00            mov qword ptr [rip + 0x1e24f4], rax
00C1E33C  48 8D 05 9D 0F 92 FF            lea rax, [rip - 0x6df063]
00C1E343  48 89 05 F6 24 1E 00            mov qword ptr [rip + 0x1e24f6], rax
00C1E34A  C3                              ret
00C1E34B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInitNonBusHandler(void)
{
    *(unsigned __int64 *)(v_rip + 1975546) = v_rip - 8069015;
    *(unsigned __int64 *)(v_rip + 1975540) = v_rip - 1679365;
    *(unsigned __int64 *)(v_rip + 1975542) = v_rip - 7204963;
    return v_rip - 7204963;
}
```

## 5. (Beta) C Style

```c
void HalpInitNonBusHandler(void)
{
    *(uint64_t *)(v_rip + 0x1E24FA) = v_rip - 8069015;
    *(uint64_t *)(v_rip + 0x1E24F4) = v_rip - 1679365;
    *(uint64_t *)(v_rip + 0x1E24F6) = v_rip - 7204963;
    return v_rip - 7204963;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1E320&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C1E320[BB_00C1E320]
  bb_00C1E34B[BB_00C1E34B]
```
