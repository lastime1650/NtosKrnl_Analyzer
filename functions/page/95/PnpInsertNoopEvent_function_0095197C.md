# PnpInsertNoopEvent

- RVA: `0x0095197C`–`0x009519E1` (길이 `101` bytes)
- VA: `0x000000014095197C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `24`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00951991` → [PnpCreateDeviceEventEntry](PnpCreateDeviceEventEntry_function_00951B48.md) (function, `0x00951B48`)
- `0x009519C9` → [PnpInsertEventInQueue](PnpInsertEventInQueue_function_00951B78.md) (function, `0x00951B78`)

### Direct callers
- [PnpDeferNotification](PnpDeferNotification_function_00951888.md) at `0x0095194E`

### Static image references
- `0x009519A2` → RVA `0x00014D68` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0095197C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00951981  57                              push rdi
00951982  48 83 EC 20                     sub rsp, 0x20
00951986  48 8B F9                        mov rdi, rcx
00951989  48 8B DA                        mov rbx, rdx
0095198C  B9 C8 00 00 00                  mov ecx, 0xc8
00951991  E8 B2 01 00 00                  call 0x140951b48
00951996  48 85 C0                        test rax, rax
00951999  74 3F                           je 0x1409519da
0095199B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0095199F  48 8B C8                        mov rcx, rax
009519A2  0F 10 05 BF 33 6C FF            movups xmm0, xmmword ptr [rip - 0x93cc41]
009519A9  C7 80 88 00 00 00 01 00 00 00   mov dword ptr [rax + 0x88], 1
009519B3  48 89 98 90 00 00 00            mov qword ptr [rax + 0x90], rbx
009519BA  F3 0F 7F 40 78                  movdqu xmmword ptr [rax + 0x78], xmm0
009519BF  C7 80 9C 00 00 00 50 00 00 00   mov dword ptr [rax + 0x9c], 0x50
009519C9  E8 AA 01 00 00                  call 0x140951b78
009519CE  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009519D3  48 83 C4 20                     add rsp, 0x20
009519D7  5F                              pop rdi
009519D8  C3                              ret
009519D9  CC                              int3
009519DA  B8 9A 00 00 C0                  mov eax, 0xc000009a
009519DF  EB ED                           jmp 0x1409519ce
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpInsertNoopEvent(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = PnpCreateDeviceEventEntry(200, a2, a3, a4);
    if (result == 0) goto loc_009519DA;
    *(unsigned __int64 *)(result + 24) = a1;
    *(unsigned int *)(result + 136) = 1;
    *(unsigned __int64 *)(result + 144) = a2;
    *(unsigned __int64 *)(result + 120) = v_xmm0;
    *(unsigned int *)(result + 156) = 80;
    result = PnpInsertEventInQueue(result, a2, a3, a4);
loc_009519CE:
    v_rsp = (v_rsp) + (32);
    return result;
loc_009519DA:
    goto loc_009519CE;
}
```

## 5. (Beta) C Style

```c
int64_t PnpInsertNoopEvent(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = PnpCreateDeviceEventEntry(200, Arg2, a3, a4);
    if (result == 0) goto loc_009519DA;
    *(uint64_t *)(result + 0x18) = Arg1;
    *(uint32_t *)(result + 0x88) = 1;
    *(uint64_t *)(result + 0x90) = Arg2;
    *(uint64_t *)(result + 0x78) = v_xmm0;
    *(uint32_t *)(result + 0x9C) = 80;
    result = PnpInsertEventInQueue(result, Arg2, a3, a4);
loc_009519CE:
    local_rsp = (local_rsp) + (32);
    return result;
loc_009519DA:
    goto loc_009519CE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0095197C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0095197C[BB_0095197C]
  bb_0095199B[BB_0095199B]
  bb_009519CE[BB_009519CE]
  bb_009519D9[BB_009519D9]
  bb_009519DA[BB_009519DA]
  bb_0095197C -->|branch| bb_009519DA
  bb_0095197C -->|fallthrough| bb_0095199B
  bb_0095199B -->|flow| bb_009519CE
  bb_009519D9 -->|flow| bb_009519DA
  bb_009519DA -->|branch| bb_009519CE
```
