# sub_006E1EB6

- RVA: `0x006E1EB6`–`0x006E1EC7` (길이 `17` bytes)
- VA: `0x00000001406E1EB6`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000761C4`
- 디코드: `4`개 명령, `17/17` bytes 표시
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
  - `0x006E1EB9` → [sub_0032BCD2 + 0x26](../32/Unknown_function_0032BCD2.md) (`tail-transfer`)
  - `0x006E1EC2` → [sub_0032BCD2 + 0x26](../32/Unknown_function_0032BCD2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E1EB6  83 FA 01                        cmp edx, 1
006E1EB9  0F 85 39 9E C4 FF               jne 0x14032bcf8
006E1EBF  83 C8 08                        or eax, 8
006E1EC2  E9 31 9E C4 FF                  jmp 0x14032bcf8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E1EB6(__int64 a1, int a2)
{
    __int64 result;

    result = (unsigned int)((result) | (8));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E1EB6(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    result = (uint32_t)((result) | (8));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E1EB6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E1EB6[BB_006E1EB6]
  bb_006E1EBF[BB_006E1EBF]
  bb_006E1EB6 -->|fallthrough| bb_006E1EBF
```
