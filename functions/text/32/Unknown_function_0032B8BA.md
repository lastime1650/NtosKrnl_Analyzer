# sub_0032B8BA

- RVA: `0x0032B8BA`–`0x0032B8CD` (길이 `19` bytes)
- VA: `0x000000014032B8BA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076104`
- 디코드: `6`개 명령, `19/19` bytes 표시
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
  - `0x0032B8C5` → [MiAccessCheck + 0xA0](MiAccessCheck_function_0032B720.md) (`tail-transfer`)
  - `0x0032B8CB` → [MiAccessCheck + 0x14E](MiAccessCheck_function_0032B720.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0032B8BA  CC                              int3
0032B8BB  48 8B C1                        mov rax, rcx
0032B8BE  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0032B8C2  80 38 01                        cmp byte ptr [rax], 1
0032B8C5  0F 84 F5 FE FF FF               je 0x14032b7c0
0032B8CB  EB A1                           jmp 0x14032b86e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0032B8BA(__int64 a1)
{
    __int64 result;

    result = (a1) & (-2);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0032B8BA(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (Arg1) & (-2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0032B8BA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0032B8BA[BB_0032B8BA]
  bb_0032B8CB[BB_0032B8CB]
  bb_0032B8BA -->|fallthrough| bb_0032B8CB
```
