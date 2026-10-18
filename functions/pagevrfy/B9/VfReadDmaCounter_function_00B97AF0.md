# VfReadDmaCounter

- RVA: `0x00B97AF0`–`0x00B97B2C` (길이 `60` bytes)
- VA: `0x0000000140B97AF0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `19`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B97AFB` → [ViGetAdapterInformationInternal](ViGetAdapterInformationInternal_function_00B98E88.md) (function, `0x00B98E88`)
- `0x00B97B05` → [VF_ASSERT_MAX_IRQL](VF_ASSERT_MAX_IRQL_function_00B94FB0.md) (function, `0x00B94FB0`)
- `0x00B97B0D` → [ViGetRealDmaAdapter](ViGetRealDmaAdapter_function_00B990DC.md) (function, `0x00B990DC`)
- `0x00B97B20` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B97B20` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B97AF0  40 53                           push rbx
00B97AF2  48 83 EC 20                     sub rsp, 0x20
00B97AF6  B2 01                           mov dl, 1
00B97AF8  48 8B D9                        mov rbx, rcx
00B97AFB  E8 88 13 00 00                  call 0x140b98e88
00B97B00  48 85 C0                        test rax, rax
00B97B03  74 05                           je 0x140b97b0a
00B97B05  E8 A6 D4 FF FF                  call 0x140b94fb0
00B97B0A  48 8B CB                        mov rcx, rbx
00B97B0D  E8 CA 15 00 00                  call 0x140b990dc
00B97B12  48 8B D0                        mov rdx, rax
00B97B15  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00B97B19  48 8B 41 50                     mov rax, qword ptr [rcx + 0x50]
00B97B1D  48 8B CA                        mov rcx, rdx
00B97B20  E8 AB 2F B2 FF                  call 0x1406baad0
00B97B25  48 83 C4 20                     add rsp, 0x20
00B97B29  5B                              pop rbx
00B97B2A  C3                              ret
00B97B2B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfReadDmaCounter(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ViGetAdapterInformationInternal(a1, 1, a3, a4);
    if (result != 0) {
        result = VF_ASSERT_MAX_IRQL(a1, 1, a3, a4);
    }
    result = ViGetRealDmaAdapter(a1, 1, a3, a4);
    result = guard_dispatch_icall(result, result, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfReadDmaCounter(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ViGetAdapterInformationInternal(Arg1, 1, a3, a4);
    if (result != 0) {
        result = VF_ASSERT_MAX_IRQL(Arg1, 1, a3, a4);
    }
    result = ViGetRealDmaAdapter(Arg1, 1, a3, a4);
    result = guard_dispatch_icall(result, result, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B97AF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B97AF0[BB_00B97AF0]
  bb_00B97B05[BB_00B97B05]
  bb_00B97B0A[BB_00B97B0A]
  bb_00B97B2B[BB_00B97B2B]
  bb_00B97AF0 -->|branch| bb_00B97B0A
  bb_00B97AF0 -->|fallthrough| bb_00B97B05
  bb_00B97B05 -->|flow| bb_00B97B0A
```
