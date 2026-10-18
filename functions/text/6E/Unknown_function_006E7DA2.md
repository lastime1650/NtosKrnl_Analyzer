# sub_006E7DA2

- RVA: `0x006E7DA2`–`0x006E7DBA` (길이 `24` bytes)
- VA: `0x00000001406E7DA2`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DF4C`
- 디코드: `5`개 명령, `24/24` bytes 표시
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
  - `0x006E7DA7` → [PPmHeteroHgsUpdateOrderValue + 0xEC](../3B/PPmHeteroHgsUpdateOrderValue_function_003BFD24.md) (`tail-transfer`)
  - `0x006E7DB5` → [PPmHeteroHgsUpdateOrderValue + 0xEC](../3B/PPmHeteroHgsUpdateOrderValue_function_003BFD24.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E7DA2  46 38 64 B1 05                  cmp byte ptr [rcx + r14*4 + 5], r12b
006E7DA7  0F 84 63 80 CD FF               je 0x1403bfe10
006E7DAD  44 8A FB                        mov r15b, bl
006E7DB0  46 88 64 B1 05                  mov byte ptr [rcx + r14*4 + 5], r12b
006E7DB5  E9 56 80 CD FF                  jmp 0x1403bfe10
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006E7DA2(__int64 a1)
{
    *(unsigned __int8 *)(a1 + v_r14 * 4 + 5) = (unsigned __int8)(v_r12);
}
```

## 5. (Beta) C Style

```c
void sub_006E7DA2(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint8_t *)(arg1 + local_r14 * 4 + 0x5) = (uint8_t)(local_r12);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x5 + r14*4` | `8` | `R` |
| `Arg1` | `+ 0x5 + r14*4` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E7DA2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E7DA2[BB_006E7DA2]
  bb_006E7DAD[BB_006E7DAD]
  bb_006E7DA2 -->|fallthrough| bb_006E7DAD
```
