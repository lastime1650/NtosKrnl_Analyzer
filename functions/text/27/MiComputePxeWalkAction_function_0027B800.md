# MiComputePxeWalkAction

- RVA: `0x0027B800`–`0x0027B826` (길이 `38` bytes)
- VA: `0x000000014027B800`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066010`
- 디코드: `13`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiWalkPageTablesRecursively](MiWalkPageTablesRecursively_function_002796C0.md) at `0x00279A32`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0027B824` → [sub_0027B888](Unknown_function_0027B888.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0027B800  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0027B805  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
0027B80A  56                              push rsi
0027B80B  57                              push rdi
0027B80C  41 56                           push r14
0027B80E  48 83 EC 20                     sub rsp, 0x20
0027B812  48 8B 1A                        mov rbx, qword ptr [rdx]
0027B815  45 8B F1                        mov r14d, r9d
0027B818  49 63 E8                        movsxd rbp, r8d
0027B81B  48 8B FA                        mov rdi, rdx
0027B81E  48 8B F1                        mov rsi, rcx
0027B821  83 FD 03                        cmp ebp, 3
0027B824  74 62                           je 0x14027b888
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiComputePxeWalkAction(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_stack_p20 = v_rbp;
    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void MiComputePxeWalkAction(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t local_rsp;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    v_stack_p20 = local_rbp;
    local_rsp = (local_rsp) - (32);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0027B800&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0027B800[BB_0027B800]
```
