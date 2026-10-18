# IoGetSiloParameters

- RVA: `0x0043E220`–`0x0043E234` (길이 `20` bytes)
- VA: `0x000000014043E220`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `20/20` bytes 표시
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
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043E220  48 8B 81 D0 00 00 00            mov rax, qword ptr [rcx + 0xd0]
0043E227  48 85 C0                        test rax, rax
0043E22A  74 06                           je 0x14043e232
0043E22C  48 8B 40 40                     mov rax, qword ptr [rax + 0x40]
0043E230  C3                              ret
0043E231  CC                              int3
0043E232  C3                              ret
0043E233  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetSiloParameters(__int64 a1)
{
    if (*(unsigned __int64 *)(a1 + 208) == 0) goto loc_0043E232;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 64);
loc_0043E232:
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 64);
}
```

## 5. (Beta) C Style

```c
int64_t IoGetSiloParameters(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (*(uint64_t *)(arg1 + 0xD0) == 0) goto loc_0043E232;
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0xD0) + 0x40);
loc_0043E232:
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0xD0) + 0x40);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043E220&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043E220[BB_0043E220]
  bb_0043E22C[BB_0043E22C]
  bb_0043E231[BB_0043E231]
  bb_0043E232[BB_0043E232]
  bb_0043E233[BB_0043E233]
  bb_0043E220 -->|branch| bb_0043E232
  bb_0043E220 -->|fallthrough| bb_0043E22C
  bb_0043E231 -->|flow| bb_0043E232
```
