# CmpSearchAndRehashWorker

- RVA: `0x007EB1A0`–`0x007EB1CB` (길이 `43` bytes)
- VA: `0x00000001407EB1A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007EB1AF` → [CmpRehashKcbSubtree](CmpRehashKcbSubtree_function_007EB0C4.md) (function, `0x007EB0C4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007EB1A0  40 53                           push rbx
007EB1A2  48 83 EC 20                     sub rsp, 0x20
007EB1A6  48 8B DA                        mov rbx, rdx
007EB1A9  48 8B D1                        mov rdx, rcx
007EB1AC  48 8B 0B                        mov rcx, qword ptr [rbx]
007EB1AF  E8 10 FF FF FF                  call 0x1407eb0c4
007EB1B4  33 C9                           xor ecx, ecx
007EB1B6  84 C0                           test al, al
007EB1B8  74 08                           je 0x1407eb1c2
007EB1BA  FF 43 08                        inc dword ptr [rbx + 8]
007EB1BD  B9 02 00 00 00                  mov ecx, 2
007EB1C2  8B C1                           mov eax, ecx
007EB1C4  48 83 C4 20                     add rsp, 0x20
007EB1C8  5B                              pop rbx
007EB1C9  C3                              ret
007EB1CA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpSearchAndRehashWorker(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = CmpRehashKcbSubtree(*(unsigned __int64 *)(a2), a1, a3, a4);
    a1 = 0;
    if ((unsigned __int8)(result) != 0) {
        a1 = 2;
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(a1));
}
```

## 5. (Beta) C Style

```c
int64_t CmpSearchAndRehashWorker(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = CmpRehashKcbSubtree(*(uint64_t *)(arg2), Arg1, a3, a4);
    Arg1 = 0;
    if ((uint8_t)(result) != 0) {
        Arg1 = 2;
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(Arg1));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007EB1A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007EB1A0[BB_007EB1A0]
  bb_007EB1BA[BB_007EB1BA]
  bb_007EB1C2[BB_007EB1C2]
  bb_007EB1CA[BB_007EB1CA]
  bb_007EB1A0 -->|branch| bb_007EB1C2
  bb_007EB1A0 -->|fallthrough| bb_007EB1BA
  bb_007EB1BA -->|flow| bb_007EB1C2
```
