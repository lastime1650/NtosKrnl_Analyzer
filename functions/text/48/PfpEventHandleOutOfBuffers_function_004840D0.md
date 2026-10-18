# PfpEventHandleOutOfBuffers

- RVA: `0x004840D0`–`0x004840FA` (길이 `42` bytes)
- VA: `0x00000001404840D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004840E4` → [PfFbBufferListAllocateTemporary](PfFbBufferListAllocateTemporary_function_00484100.md) (function, `0x00484100`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004840D0  40 53                           push rbx
004840D2  48 83 EC 20                     sub rsp, 0x20
004840D6  48 8B C2                        mov rax, rdx
004840D9  48 8B D9                        mov rbx, rcx
004840DC  48 8B C8                        mov rcx, rax
004840DF  BA 00 08 00 00                  mov edx, 0x800
004840E4  E8 17 00 00 00                  call 0x140484100
004840E9  85 C0                           test eax, eax
004840EB  79 06                           jns 0x1404840f3
004840ED  FF 83 B4 02 00 00               inc dword ptr [rbx + 0x2b4]
004840F3  48 83 C4 20                     add rsp, 0x20
004840F7  5B                              pop rbx
004840F8  C3                              ret
004840F9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpEventHandleOutOfBuffers(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PfFbBufferListAllocateTemporary(a2, (unsigned int)(0x800ULL), a3, a4);
    if (sign_flag) {
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfpEventHandleOutOfBuffers(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PfFbBufferListAllocateTemporary(Arg2, (uint32_t)(0x800ULL), a3, a4);
    if (sign_flag) {
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2B4` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004840D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004840D0[BB_004840D0]
  bb_004840ED[BB_004840ED]
  bb_004840F3[BB_004840F3]
  bb_004840F9[BB_004840F9]
  bb_004840D0 -->|branch| bb_004840F3
  bb_004840D0 -->|fallthrough| bb_004840ED
  bb_004840ED -->|flow| bb_004840F3
```
