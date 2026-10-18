# sub_00B2DBCA

- RVA: `0x00B2DBCA`–`0x00B2DBE9` (길이 `31` bytes)
- VA: `0x0000000140B2DBCA`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009E320`
- 디코드: `7`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B2DBCE` → [CmpTransMgrRollback](../9B/CmpTransMgrRollback_function_009B1400.md) (function, `0x009B1400`)
- `0x00B2DBDE` → [TmPrepareComplete](../../text/4F/TmPrepareComplete_function_004FE200.md) (function, `0x004FE200`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B2DBDE` → [TmPrepareComplete](../../text/4F/TmPrepareComplete_function_004FE200.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B2DBD9` → [CmKtmNotification + 0x15D](../9B/CmKtmNotification_function_009B1950.md) (`tail-transfer`)
  - `0x00B2DBE4` → [CmKtmNotification + 0x310](../9B/CmKtmNotification_function_009B1950.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B2DBCA  48 8D 55 8F                     lea rdx, [rbp - 0x71]
00B2DBCE  E8 2D 38 E8 FF                  call 0x1409b1400
00B2DBD3  41 B8 08 00 00 00               mov r8d, 8
00B2DBD9  E9 CF 3E E8 FF                  jmp 0x1409b1aad
00B2DBDE  E8 1D 06 9D FF                  call 0x1404fe200
00B2DBE3  90                              nop
00B2DBE4  E9 77 40 E8 FF                  jmp 0x1409b1c60
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B2DBCA(void)
{
    __int64 result;

    result = CmpTransMgrRollback(a1, v_rbp - 113, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B2DBCA(void)
{
    int64_t result;

    result = CmpTransMgrRollback(a1, local_rbp - 113, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B2DBCA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B2DBCA[BB_00B2DBCA]
  bb_00B2DBDE[BB_00B2DBDE]
```
