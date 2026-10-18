# sub_009349BE

- RVA: `0x009349BE`–`0x009349D6` (길이 `24` bytes)
- VA: `0x00000001409349BE`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008F190`
- 디코드: `10`개 명령, `24/24` bytes 표시
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
009349BE  48 89 01                        mov qword ptr [rcx], rax
009349C1  49 8B C5                        mov rax, r13
009349C4  4D 85 C9                        test r9, r9
009349C7  74 03                           je 0x1409349cc
009349C9  4D 89 21                        mov qword ptr [r9], r12
009349CC  48 83 C4 68                     add rsp, 0x68
009349D0  41 5D                           pop r13
009349D2  41 5C                           pop r12
009349D4  C3                              ret
009349D5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009349BE(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 v_rsp;

    *(unsigned __int64 *)(a1) = result;
    if (a4 != 0) {
        *(unsigned __int64 *)(a4) = v_r12;
    }
    v_rsp = (v_rsp) + (104);
    return v_r13;
}
```

## 5. (Beta) C Style

```c
int64_t sub_009349BE(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    *(uint64_t *)(arg1) = result;
    if (Arg4 != 0) {
        *(uint64_t *)(Arg4) = local_r12;
    }
    local_rsp = (local_rsp) + (104);
    return local_r13;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009349BE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009349BE[BB_009349BE]
  bb_009349C9[BB_009349C9]
  bb_009349CC[BB_009349CC]
  bb_009349D5[BB_009349D5]
  bb_009349BE -->|branch| bb_009349CC
  bb_009349BE -->|fallthrough| bb_009349C9
  bb_009349C9 -->|flow| bb_009349CC
```
