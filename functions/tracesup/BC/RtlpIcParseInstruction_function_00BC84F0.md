# RtlpIcParseInstruction

- RVA: `0x00BC84F0`–`0x00BC8513` (길이 `35` bytes)
- VA: `0x0000000140BC84F0`
- 실행 섹션: `TRACESUP`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BC84F9` → [RtlpIcParseInstructionPrefix](RtlpIcParseInstructionPrefix_function_00BC851C.md) (function, `0x00BC851C`)
- `0x00BC8507` → [RtlpIcEmulateInstruction](RtlpIcEmulateInstruction_function_00BC7A08.md) (function, `0x00BC7A08`)

### Direct callers
- [RtlIcParseInstruction](RtlIcParseInstruction_function_00BC70E8.md) at `0x00BC713A`
- [RtlIcParseInstruction](RtlIcParseInstruction_function_00BC70E8.md) at `0x00BC717B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC84F0  40 53                           push rbx
00BC84F2  48 83 EC 20                     sub rsp, 0x20
00BC84F6  48 8B D9                        mov rbx, rcx
00BC84F9  E8 1E 00 00 00                  call 0x140bc851c
00BC84FE  85 C0                           test eax, eax
00BC8500  78 0A                           js 0x140bc850c
00BC8502  33 D2                           xor edx, edx
00BC8504  48 8B CB                        mov rcx, rbx
00BC8507  E8 FC F4 FF FF                  call 0x140bc7a08
00BC850C  48 83 C4 20                     add rsp, 0x20
00BC8510  5B                              pop rbx
00BC8511  C3                              ret
00BC8512  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpIcParseInstruction(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = RtlpIcParseInstructionPrefix(a1, a2, a3, a4);
    if (!(sign_flag)) {
        a2 = 0;
        a1 = a1;
        result = RtlpIcEmulateInstruction(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpIcParseInstruction(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = RtlpIcParseInstructionPrefix(Arg1, Arg2, a3, a4);
    if (!(sign_flag)) {
        Arg2 = 0;
        Arg1 = Arg1;
        result = RtlpIcEmulateInstruction(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=tracesup&rva=0x00BC84F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC84F0[BB_00BC84F0]
  bb_00BC8502[BB_00BC8502]
  bb_00BC850C[BB_00BC850C]
  bb_00BC8512[BB_00BC8512]
  bb_00BC84F0 -->|branch| bb_00BC850C
  bb_00BC84F0 -->|fallthrough| bb_00BC8502
  bb_00BC8502 -->|flow| bb_00BC850C
```
