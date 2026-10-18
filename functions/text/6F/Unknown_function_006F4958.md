# sub_006F4958

- RVA: `0x006F4958`–`0x006F496D` (길이 `21` bytes)
- VA: `0x00000001406F4958`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD1C8`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F4968` → [IopWaitForLockAlertable + 0x50](../47/IopWaitForLockAlertable_function_0047A684.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F4958  24 01                           and al, 1
006F495A  F6 D8                           neg al
006F495C  1B C0                           sbb eax, eax
006F495E  25 2B FF FF FF                  and eax, 0xffffff2b
006F4963  05 20 01 00 C0                  add eax, 0xc0000120
006F4968  E9 67 5D D8 FF                  jmp 0x14047a6d4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F4958(void)
{
    __int64 result;

    result = (unsigned __int8)((result) & (1));
    result = (unsigned __int8)(-(result));
    result = (unsigned int)((result) & (0xFFFFFF2BULL));
    result = (unsigned int)((result) + (0xC0000120ULL));
}
```

## 5. (Beta) C Style

```c
void sub_006F4958(void)
{
    int64_t result;

    result = (uint8_t)((result) & (1));
    result = (uint8_t)(-(result));
    result = (uint32_t)((result) & (0xFFFFFF2BULL));
    result = (uint32_t)((result) + (0xC0000120ULL));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F4958&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F4958[BB_006F4958]
```
