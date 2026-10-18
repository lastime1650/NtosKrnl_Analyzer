# IoTransferActivityId

- RVA: `0x004BA0D0`–`0x004BA12C` (길이 `92` bytes)
- VA: `0x00000001404BA0D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB2F8`
- 디코드: `24`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004BA0E7` → [IopIsActivityTracingEventEnabled](IopIsActivityTracingEventEnabled_function_004BA134.md) (function, `0x004BA134`)
- `0x004BA125` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004BA0E0` → RVA `0x0001C800` (`.rdata`; read)
- `0x004BA111` → RVA `0x00F8D7E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BA0D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004BA0D5  57                              push rdi
004BA0D6  48 83 EC 40                     sub rsp, 0x40
004BA0DA  48 8B F9                        mov rdi, rcx
004BA0DD  48 8B DA                        mov rbx, rdx
004BA0E0  48 8D 0D 19 27 B6 FF            lea rcx, [rip - 0x49d8e7]
004BA0E7  E8 48 00 00 00                  call 0x1404ba134
004BA0EC  84 C0                           test al, al
004BA0EE  75 0C                           jne 0x1404ba0fc
004BA0F0  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
004BA0F5  48 83 C4 40                     add rsp, 0x40
004BA0F9  5F                              pop rdi
004BA0FA  C3                              ret
004BA0FB  CC                              int3
004BA0FC  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
004BA102  48 8D 15 F7 26 B6 FF            lea rdx, [rip - 0x49d909]
004BA109  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
004BA10E  45 33 C9                        xor r9d, r9d
004BA111  48 8B 0D C8 36 AD 00            mov rcx, qword ptr [rip + 0xad36c8]
004BA118  45 33 C0                        xor r8d, r8d
004BA11B  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
004BA120  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
004BA125  E8 A6 4F DA FF                  call 0x14025f0d0
004BA12A  EB C4                           jmp 0x1404ba0f0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoTransferActivityId(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (64);
    result = IopIsActivityTracingEventEnabled(v_rip - 4839655, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_004BA0FC;
loc_004BA0F0:
    v_rsp = (v_rsp) + (64);
    return result;
loc_004BA0FC:
    a4 = 0;
    a3 = 0;
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = a1;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 11351752), v_rip - 4839689, a3, a4);
    goto loc_004BA0F0;
}
```

## 5. (Beta) C Style

```c
int64_t IoTransferActivityId(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (64);
    result = IopIsActivityTracingEventEnabled(v_rip - 4839655, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_004BA0FC;
loc_004BA0F0:
    local_rsp = (local_rsp) + (64);
    return result;
loc_004BA0FC:
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = Arg1;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xAD36C8), v_rip - 4839689, Arg3, Arg4);
    goto loc_004BA0F0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BA0D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BA0D0[BB_004BA0D0]
  bb_004BA0F0[BB_004BA0F0]
  bb_004BA0FB[BB_004BA0FB]
  bb_004BA0FC[BB_004BA0FC]
  bb_004BA0D0 -->|branch| bb_004BA0FC
  bb_004BA0D0 -->|fallthrough| bb_004BA0F0
  bb_004BA0FB -->|flow| bb_004BA0FC
  bb_004BA0FC -->|branch| bb_004BA0F0
```
