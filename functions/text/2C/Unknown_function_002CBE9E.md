# sub_002CBE9E

- RVA: `0x002CBE9E`–`0x002CBEB8` (길이 `26` bytes)
- VA: `0x00000001402CBE9E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F3DC`
- 디코드: `5`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002CBE9E` → RVA `0x00FC5000` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002CBEB3` → [sub_002CBCDC + 0x4A](Unknown_function_002CBCDC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002CBE9E  0F B7 05 5B 91 CF 00            movzx eax, word ptr [rip + 0xcf915b]
002CBEA5  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
002CBEA9  48 69 F8 80 DF 00 00            imul rdi, rax, 0xdf80
002CBEB0  48 03 FA                        add rdi, rdx
002CBEB3  E9 6E FE FF FF                  jmp 0x1402cbd26
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002CBE9E(__int64 a1)
{
    __int64 v_rdi;

    v_rdi = (v_rdi) * (*(unsigned __int16 *)(v_rip + 13603163));
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a1 + 16));
}
```

## 5. (Beta) C Style

```c
int64_t sub_002CBE9E(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rdi;

    local_rdi = (local_rdi) * (*(uint16_t *)(v_rip + 0xCF915B));
    local_rdi = (local_rdi) + (*(uint64_t *)(arg1 + 0x10));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CBE9E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002CBE9E[BB_002CBE9E]
```
