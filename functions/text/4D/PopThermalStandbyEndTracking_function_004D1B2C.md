# PopThermalStandbyEndTracking

- RVA: `0x004D1B2C`–`0x004D1B7D` (길이 `81` bytes)
- VA: `0x00000001404D1B2C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `81/81` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x004D1B72` → [PopTraceThermalStandbyComplete](../5D/PopTraceThermalStandbyComplete_function_005D7E74.md) (function, `0x005D7E74`)

### Direct callers
- [PopThermalCsEntry](../42/PopThermalCsEntry_function_0042FE14.md) at `0x0042FE9B`
- [PopThermalSxEntry](../4E/PopThermalSxEntry_function_004E3D20.md) at `0x004E3D59`
- [PopThermalCsExit](../5D/PopThermalCsExit_function_005D54C8.md) at `0x005D54DD`
- [sub_006F9E40](../6F/Unknown_function_006F9E40.md) at `0x006F9F8D`
- [PopThermalStateTransitionWorker](../../page/75/PopThermalStateTransitionWorker_function_0075F820.md) at `0x0075F8D5`

### Static image references
- `0x004D1B30` → RVA `0x00F0BB1C` (`.data`; read)
- `0x004D1B39` → RVA `0x00F0BB1D` (`.data`; read)
- `0x004D1B3F` → RVA `0x00F0BB1C` (`.data`; write)
- `0x004D1B47` → RVA `0x00F0BB1D` (`.data`; write)
- `0x004D1B64` → RVA `0x00F0BB20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D1B2C  48 83 EC 28                     sub rsp, 0x28
004D1B30  44 8A 05 E5 9F A3 00            mov r8b, byte ptr [rip + 0xa39fe5]
004D1B37  33 C0                           xor eax, eax
004D1B39  38 05 DE 9F A3 00               cmp byte ptr [rip + 0xa39fde], al
004D1B3F  88 05 D7 9F A3 00               mov byte ptr [rip + 0xa39fd7], al
004D1B45  74 30                           je 0x1404d1b77
004D1B47  88 05 D0 9F A3 00               mov byte ptr [rip + 0xa39fd0], al
004D1B4D  48 BA 08 00 00 00 80 F7 FF FF   movabs rdx, 0xfffff78000000008
004D1B57  48 B8 BD 42 7A E5 D5 94 BF D6   movabs rax, 0xd6bf94d5e57a42bd
004D1B61  48 8B 12                        mov rdx, qword ptr [rdx]
004D1B64  48 2B 15 B5 9F A3 00            sub rdx, qword ptr [rip + 0xa39fb5]
004D1B6B  48 F7 E2                        mul rdx
004D1B6E  48 C1 EA 17                     shr rdx, 0x17
004D1B72  E8 FD 62 10 00                  call 0x1405d7e74
004D1B77  48 83 C4 28                     add rsp, 0x28
004D1B7B  C3                              ret
004D1B7C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopThermalStandbyEndTracking(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    *(unsigned __int8 *)(v_rip + 10723287) = 0;
    if ((*(unsigned __int8 *)(v_rip + 10723294)) != 0) {
        *(unsigned __int8 *)(v_rip + 10723280) = 0;
        a2 = *(unsigned __int64 *)(a2);
        a2 = (a2) - (*(unsigned __int64 *)(v_rip + 10723253));
        a2 = (a2) >> (23);
        result = PopTraceThermalStandbyComplete(a1, a2, *(unsigned __int8 *)(v_rip + 10723301), a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopThermalStandbyEndTracking(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    *(uint8_t *)(v_rip + 0xA39FD7) = 0;
    if ((*(uint8_t *)(v_rip + 0xA39FDE)) != 0) {
        *(uint8_t *)(v_rip + 0xA39FD0) = 0;
        a2 = *(uint64_t *)(a2);
        a2 = (a2) - (*(uint64_t *)(v_rip + 0xA39FB5));
        a2 = (a2) >> (23);
        result = PopTraceThermalStandbyComplete(a1, a2, *(uint8_t *)(v_rip + 0xA39FE5), a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D1B2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D1B2C[BB_004D1B2C]
  bb_004D1B47[BB_004D1B47]
  bb_004D1B77[BB_004D1B77]
  bb_004D1B7C[BB_004D1B7C]
  bb_004D1B2C -->|branch| bb_004D1B77
  bb_004D1B2C -->|fallthrough| bb_004D1B47
  bb_004D1B47 -->|flow| bb_004D1B77
```
