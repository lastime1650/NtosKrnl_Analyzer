# ViRlrsMmProbeAndLockPages_Entry

- RVA: `0x00BAF7C0`–`0x00BAF7E1` (길이 `33` bytes)
- VA: `0x0000000140BAF7C0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BAF7C6` → [VfFaultsInjectResourceFailure](VfFaultsInjectResourceFailure_function_00BA6558.md) (function, `0x00BA6558`)
- `0x00BAF7D5` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BAF7D5` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAF7C0  48 83 EC 28                     sub rsp, 0x28
00BAF7C4  33 C9                           xor ecx, ecx
00BAF7C6  E8 8D 6D FF FF                  call 0x140ba6558
00BAF7CB  83 F8 01                        cmp eax, 1
00BAF7CE  75 0B                           jne 0x140baf7db
00BAF7D0  B9 A1 00 00 C0                  mov ecx, 0xc00000a1
00BAF7D5  E8 76 72 74 FF                  call 0x1402f6a50
00BAF7DA  CC                              int3
00BAF7DB  48 83 C4 28                     add rsp, 0x28
00BAF7DF  C3                              ret
00BAF7E0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViRlrsMmProbeAndLockPages_Entry(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = 0;
    result = VfFaultsInjectResourceFailure(a1, a2, a3, a4);
    if (((unsigned int)(result)) == 1) {
        a1 = 0xC00000A1ULL;
        result = RtlRaiseStatus(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViRlrsMmProbeAndLockPages_Entry(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = 0;
    result = VfFaultsInjectResourceFailure(Arg1, a2, a3, a4);
    if (((uint32_t)(result)) == 1) {
        Arg1 = 0xC00000A1ULL;
        result = RtlRaiseStatus(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAF7C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAF7C0[BB_00BAF7C0]
  bb_00BAF7D0[BB_00BAF7D0]
  bb_00BAF7DB[BB_00BAF7DB]
  bb_00BAF7E0[BB_00BAF7E0]
  bb_00BAF7C0 -->|branch| bb_00BAF7DB
  bb_00BAF7C0 -->|fallthrough| bb_00BAF7D0
  bb_00BAF7D0 -->|flow| bb_00BAF7DB
```
