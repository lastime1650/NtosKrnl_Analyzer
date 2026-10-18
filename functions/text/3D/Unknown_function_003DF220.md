# sub_003DF220

- RVA: `0x003DF220`–`0x003DF230` (길이 `16` bytes)
- VA: `0x00000001403DF220`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009475C`
- 디코드: `4`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003DF226` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003DF22B` → [sub_003DF08F + 0x91](Unknown_function_003DF08F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003DF220  48 8B D1                        mov rdx, rcx
003DF223  48 8B CB                        mov rcx, rbx
003DF226  E8 15 76 2E 00                  call 0x1406c6840
003DF22B  E9 F0 FE FF FF                  jmp 0x1403df120
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003DF220(__int64 a1)
{
    __int64 result;

    result = memcpy(v_rbx, a1, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_003DF220(int64_t Arg1)
{
    int64_t result;

    result = memcpy(local_rbx, Arg1, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DF220&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DF220[BB_003DF220]
```
