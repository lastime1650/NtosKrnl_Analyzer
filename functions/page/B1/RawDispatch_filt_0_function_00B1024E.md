# RawDispatch$filt$0

- RVA: `0x00B1024E`–`0x00B10271` (길이 `35` bytes)
- VA: `0x0000000140B1024E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009C408`
- 디코드: `14`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B1025C` → [FsRtlIsNtstatusExpected](../../text/26/FsRtlIsNtstatusExpected_function_0026D390.md) (function, `0x0026D390`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B1025C` → [FsRtlIsNtstatusExpected](../../text/26/FsRtlIsNtstatusExpected_function_0026D390.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B1024E  40 55                           push rbp
00B10250  48 83 EC 30                     sub rsp, 0x30
00B10254  48 8B EA                        mov rbp, rdx
00B10257  48 8B 01                        mov rax, qword ptr [rcx]
00B1025A  8B 08                           mov ecx, dword ptr [rax]
00B1025C  E8 2F D1 75 FF                  call 0x14026d390
00B10261  33 C9                           xor ecx, ecx
00B10263  84 C0                           test al, al
00B10265  0F 95 C1                        setne cl
00B10268  8B C1                           mov eax, ecx
00B1026A  48 83 C4 30                     add rsp, 0x30
00B1026E  5D                              pop rbp
00B1026F  C3                              ret
00B10270  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RawDispatch_filt_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    result = FsRtlIsNtstatusExpected((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))), a2, a3, a4);
    a1 = 0;
    a1 = ((unsigned __int8)(result) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)(a1));
}
```

## 5. (Beta) C Style

```c
int64_t RawDispatch_filt_0(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    result = FsRtlIsNtstatusExpected((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))), Arg2, a3, a4);
    Arg1 = 0;
    Arg1 = ((uint8_t)(result) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)(Arg1));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1024E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B1024E[BB_00B1024E]
  bb_00B10270[BB_00B10270]
```
