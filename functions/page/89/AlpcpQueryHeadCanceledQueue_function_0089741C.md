# AlpcpQueryHeadCanceledQueue

- RVA: `0x0089741C`–`0x0089743E` (길이 `34` bytes)
- VA: `0x000000014089741C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [AlpcpReceiveMessagePort](AlpcpReceiveMessagePort_function_00896B40.md) at `0x00896C3C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0089741C  48 81 C1 80 01 00 00            add rcx, 0x180
00897423  48 8B 01                        mov rax, qword ptr [rcx]
00897426  48 3B C1                        cmp rax, rcx
00897429  74 0F                           je 0x14089743a
0089742B  48 8D 48 B0                     lea rcx, [rax - 0x50]
0089742F  48 F7 D8                        neg rax
00897432  48 1B C0                        sbb rax, rax
00897435  48 23 C1                        and rax, rcx
00897438  C3                              ret
00897439  CC                              int3
0089743A  33 C0                           xor eax, eax
0089743C  C3                              ret
0089743D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpQueryHeadCanceledQueue(__int64 a1)
{
    __int64 result;

    a1 = (a1) + (384);
    if ((*(unsigned __int64 *)(a1)) == a1) goto loc_0089743A;
    result = -(*(unsigned __int64 *)(a1));
    result = (result) & (*(unsigned __int64 *)(a1) - 80);
    return result;
loc_0089743A:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpQueryHeadCanceledQueue(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg1 = (Arg1) + (384);
    if ((*(uint64_t *)(arg1)) == Arg1) goto loc_0089743A;
    result = -(*(uint64_t *)(arg1));
    result = (result) & (*(uint64_t *)(arg1) - 80);
    return result;
loc_0089743A:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0089741C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0089741C[BB_0089741C]
  bb_0089742B[BB_0089742B]
  bb_00897439[BB_00897439]
  bb_0089743A[BB_0089743A]
  bb_0089743D[BB_0089743D]
  bb_0089741C -->|branch| bb_0089743A
  bb_0089741C -->|fallthrough| bb_0089742B
  bb_00897439 -->|flow| bb_0089743A
```
