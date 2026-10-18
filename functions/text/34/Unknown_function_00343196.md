# sub_00343196

- RVA: `0x00343196`–`0x003431A4` (길이 `14` bytes)
- VA: `0x0000000140343196`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077AB8`
- 디코드: `5`개 명령, `14/14` bytes 표시
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
  - `0x0034319F` → [sub_003430D1 + 0x17](Unknown_function_003430D1.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00343196  24 02                           and al, 2
00343198  F6 D8                           neg al
0034319A  1B F6                           sbb esi, esi
0034319C  83 E6 03                        and esi, 3
0034319F  E9 44 FF FF FF                  jmp 0x1403430e8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00343196(void)
{
    __int64 result;
    __int64 v_rsi;

    result = (unsigned __int8)((result) & (2));
    result = (unsigned __int8)(-(result));
    v_rsi = (unsigned int)((v_rsi) & (3));
}
```

## 5. (Beta) C Style

```c
void sub_00343196(void)
{
    int64_t result;
    int64_t local_rsi;

    result = (uint8_t)((result) & (2));
    result = (uint8_t)(-(result));
    local_rsi = (uint32_t)((local_rsi) & (3));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00343196&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00343196[BB_00343196]
```
