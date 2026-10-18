# sub_003ADA5F

- RVA: `0x003ADA5F`–`0x003ADA74` (길이 `21` bytes)
- VA: `0x00000001403ADA5F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008BD40`
- 디코드: `5`개 명령, `21/21` bytes 표시
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
  - `0x003ADA62` → [sub_003AD4D0 + 0x2C4](Unknown_function_003AD4D0.md) (`tail-transfer`)
  - `0x003ADA6F` → [sub_003AD4D0 + 0x2C4](Unknown_function_003AD4D0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003ADA5F  45 85 C9                        test r9d, r9d
003ADA62  0F 85 2C FD FF FF               jne 0x1403ad794
003ADA68  48 89 2A                        mov qword ptr [rdx], rbp
003ADA6B  48 89 6A 08                     mov qword ptr [rdx + 8], rbp
003ADA6F  E9 20 FD FF FF                  jmp 0x1403ad794
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_003ADA5F(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    *(unsigned __int64 *)(a2) = v_rbp;
    *(unsigned __int64 *)(a2 + 8) = v_rbp;
}
```

## 5. (Beta) C Style

```c
void sub_003ADA5F(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    *(uint64_t *)(arg2) = local_rbp;
    *(uint64_t *)(arg2 + 0x8) = local_rbp;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003ADA5F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003ADA5F[BB_003ADA5F]
  bb_003ADA68[BB_003ADA68]
  bb_003ADA5F -->|fallthrough| bb_003ADA68
```
