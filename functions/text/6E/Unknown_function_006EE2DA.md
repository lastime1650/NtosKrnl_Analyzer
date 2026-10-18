# sub_006EE2DA

- RVA: `0x006EE2DA`–`0x006EE305` (길이 `43` bytes)
- VA: `0x00000001406EE2DA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A124C`
- 디코드: `10`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006EE2FA` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x006EE2E3` → [MiDeprioritizeVad + 0xDC](../42/MiDeprioritizeVad_function_0042AAB4.md) (`tail-transfer`)
  - `0x006EE2F4` → [MiDeprioritizeVad + 0xDC](../42/MiDeprioritizeVad_function_0042AAB4.md) (`tail-transfer`)
  - `0x006EE300` → [MiDeprioritizeVad + 0xDC](../42/MiDeprioritizeVad_function_0042AAB4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006EE2DA  90                              nop
006EE2DB  66 83 83 E6 01 00 00 01         add word ptr [rbx + 0x1e6], 1
006EE2E3  0F 85 A7 C8 D3 FF               jne 0x14042ab90
006EE2E9  48 8D 83 98 00 00 00            lea rax, [rbx + 0x98]
006EE2F0  90                              nop
006EE2F1  48 39 00                        cmp qword ptr [rax], rax
006EE2F4  0F 84 96 C8 D3 FF               je 0x14042ab90
006EE2FA  E8 81 49 BF FF                  call 0x1402e2c80
006EE2FF  90                              nop
006EE300  E9 8B C8 D3 FF                  jmp 0x14042ab90
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006EE2DA(void)
{
    __int64 result;

    result = KiCheckForKernelApcDelivery(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006EE2DA(void)
{
    int64_t result;

    result = KiCheckForKernelApcDelivery(a1, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006EE2DA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006EE2DA[BB_006EE2DA]
  bb_006EE2E9[BB_006EE2E9]
  bb_006EE2FA[BB_006EE2FA]
  bb_006EE2DA -->|fallthrough| bb_006EE2E9
  bb_006EE2E9 -->|fallthrough| bb_006EE2FA
```
