# MiReferenceInPageFile

- RVA: `0x00380880`–`0x003808A2` (길이 `34` bytes)
- VA: `0x0000000140380880`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007B874`
- 디코드: `10`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiIssueHardFault](MiIssueHardFault_function_00380074.md) at `0x003800F6`
- [MiPfExecuteReadList](../../page/93/MiPfExecuteReadList_function_0093E1AC.md) at `0x0093E21B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0038089C` → [sub_00380934 + 0x1](Unknown_function_00380934.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00380880  40 53                           push rbx
00380882  55                              push rbp
00380883  41 57                           push r15
00380885  48 83 EC 30                     sub rsp, 0x30
00380889  48 8B 81 D0 00 00 00            mov rax, qword ptr [rcx + 0xd0]
00380890  41 8B E8                        mov ebp, r8d
00380893  44 8B FA                        mov r15d, edx
00380896  48 8B D9                        mov rbx, rcx
00380899  48 85 C0                        test rax, rax
0038089C  0F 84 93 00 00 00               je 0x140380935
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReferenceInPageFile(__int64 a1, int a2, int a3)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
}
```

## 5. (Beta) C Style

```c
int64_t MiReferenceInPageFile(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00380880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00380880[BB_00380880]
```
