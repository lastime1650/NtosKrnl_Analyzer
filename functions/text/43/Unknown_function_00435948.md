# sub_00435948

- RVA: `0x00435948`–`0x00435958` (길이 `16` bytes)
- VA: `0x0000000140435948`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A2CC0`
- 디코드: `4`개 명령, `16/16` bytes 표시
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
  - `0x00435953` → [MiUpdateDemotedSubPage + 0x42](MiUpdateDemotedSubPage_function_00435840.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00435948  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
0043594C  49 23 C5                        and rax, r13
0043594F  48 89 42 28                     mov qword ptr [rdx + 0x28], rax
00435953  E9 2A FF FF FF                  jmp 0x140435882
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00435948(__int64 a1, __int64 a2)
{
    __int64 result;

    result = (*(unsigned __int64 *)(a2 + 40)) & (v_r13);
    *(unsigned __int64 *)(a2 + 40) = result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00435948(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    result = (*(uint64_t *)(arg2 + 0x28)) & (local_r13);
    *(uint64_t *)(arg2 + 0x28) = result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00435948&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00435948[BB_00435948]
```
