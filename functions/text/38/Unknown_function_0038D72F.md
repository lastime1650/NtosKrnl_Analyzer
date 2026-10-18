# sub_0038D72F

- RVA: `0x0038D72F`–`0x0038D73D` (길이 `14` bytes)
- VA: `0x000000014038D72F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00080508`
- 디코드: `3`개 명령, `14/14` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0038D732` → [FsRtlFastUnlockSingleShared + 0x76](FsRtlFastUnlockSingleShared_function_0038D1F0.md) (`tail-transfer`)
  - `0x0038D738` → [sub_0038D588 + 0xA](Unknown_function_0038D588.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0038D72F  48 85 DB                        test rbx, rbx
0038D732  0F 84 2E FB FF FF               je 0x14038d266
0038D738  E9 55 FE FF FF                  jmp 0x14038d592
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0038D72F(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_0038D72F(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038D72F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038D72F[BB_0038D72F]
  bb_0038D738[BB_0038D738]
  bb_0038D72F -->|fallthrough| bb_0038D738
```
