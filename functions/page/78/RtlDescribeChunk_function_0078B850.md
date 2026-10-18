# RtlDescribeChunk

- RVA: `0x0078B850`–`0x0078B8A9` (길이 `89` bytes)
- VA: `0x000000014078B850`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `27`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0078B896` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0078B888` → RVA `0x00B4D750` (`RtlDescribeChunkProcs`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0078B896` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0078B850  40 53                           push rbx
0078B852  48 83 EC 30                     sub rsp, 0x30
0078B856  B8 FF 00 00 00                  mov eax, 0xff
0078B85B  4D 8B D1                        mov r10, r9
0078B85E  66 23 C8                        and cx, ax
0078B861  4D 8B D8                        mov r11, r8
0078B864  48 8B DA                        mov rbx, rdx
0078B867  66 83 F9 02                     cmp cx, 2
0078B86B  72 30                           jb 0x14078b89d
0078B86D  66 83 F9 08                     cmp cx, 8
0078B871  76 07                           jbe 0x14078b87a
0078B873  B8 5F 02 00 C0                  mov eax, 0xc000025f
0078B878  EB 28                           jmp 0x14078b8a2
0078B87A  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
0078B87F  4D 8B C2                        mov r8, r10
0078B882  0F B7 C1                        movzx eax, cx
0078B885  49 8B D3                        mov rdx, r11
0078B888  48 8D 0D C1 1E 3C 00            lea rcx, [rip + 0x3c1ec1]
0078B88F  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0078B893  48 8B CB                        mov rcx, rbx
0078B896  E8 35 F2 F2 FF                  call 0x1406baad0
0078B89B  EB 05                           jmp 0x14078b8a2
0078B89D  B8 0D 00 00 C0                  mov eax, 0xc000000d
0078B8A2  48 83 C4 30                     add rsp, 0x30
0078B8A6  5B                              pop rbx
0078B8A7  C3                              ret
0078B8A8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlDescribeChunk(unsigned __int16 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    a1 = (unsigned __int16)((a1) & (255));
    if (a1 < 2) goto loc_0078B89D;
    if (a1 <= 8) goto loc_0078B87A;
    goto loc_0078B8A2;
loc_0078B87A:
    result = guard_dispatch_icall(a2, a3, a4, a5);
    goto loc_0078B8A2;
loc_0078B89D:
loc_0078B8A2:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t RtlDescribeChunk(uint16_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    Arg1 = (uint16_t)((Arg1) & (255));
    if (Arg1 < 2) goto loc_0078B89D;
    if (Arg1 <= 8) goto loc_0078B87A;
    goto loc_0078B8A2;
loc_0078B87A:
    result = guard_dispatch_icall(Arg2, Arg3, Arg4, Arg5);
    goto loc_0078B8A2;
loc_0078B89D:
loc_0078B8A2:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(0xC000000DULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0078B850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0078B850[BB_0078B850]
  bb_0078B86D[BB_0078B86D]
  bb_0078B873[BB_0078B873]
  bb_0078B87A[BB_0078B87A]
  bb_0078B89D[BB_0078B89D]
  bb_0078B8A2[BB_0078B8A2]
  bb_0078B8A8[BB_0078B8A8]
  bb_0078B850 -->|branch| bb_0078B89D
  bb_0078B850 -->|fallthrough| bb_0078B86D
  bb_0078B86D -->|branch| bb_0078B87A
  bb_0078B86D -->|fallthrough| bb_0078B873
  bb_0078B873 -->|branch| bb_0078B8A2
  bb_0078B87A -->|branch| bb_0078B8A2
  bb_0078B89D -->|flow| bb_0078B8A2
```
