# PnpDeviceCompletionQueueAddDispatchedRequest

- RVA: `0x0049619C`–`0x0049620F` (길이 `115` bytes)
- VA: `0x000000014049619C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `29`개 명령, `115/115` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x004961B0` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004961FC` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [PipEnumerateDevice](../../page/8F/PipEnumerateDevice_function_008F99E4.md) at `0x008F9A61`
- [PnpStartDeviceNode](../../page/8F/PnpStartDeviceNode_function_008FE38C.md) at `0x008FE52D`
- [sub_00B38858](../../page/B3/Unknown_function_00B38858.md) at `0x00B388D4`

### Static image references
- `0x004961A6` → RVA `0x00F8C348` (`.data`; read)
- `0x004961B5` → RVA `0x00F8C308` (`.data`; read)
- `0x004961BC` → RVA `0x00F8C300` (`.data`; read)
- `0x004961EF` → RVA `0x00F8C310` (`.data`; read/write)
- `0x004961F5` → RVA `0x00F8C308` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049619C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004961A1  57                              push rdi
004961A2  48 83 EC 20                     sub rsp, 0x20
004961A6  48 8D 0D 9B 61 AF 00            lea rcx, [rip + 0xaf619b]
004961AD  48 8B DA                        mov rbx, rdx
004961B0  E8 BB 22 D7 FF                  call 0x140208470
004961B5  48 8B 0D 4C 61 AF 00            mov rcx, qword ptr [rip + 0xaf614c]
004961BC  48 8D 15 3D 61 AF 00            lea rdx, [rip + 0xaf613d]
004961C3  33 FF                           xor edi, edi
004961C5  48 39 15 34 61 AF 00            cmp qword ptr [rip + 0xaf6134], rdx
004961CC  40 0F 94 C7                     sete dil
004961D0  48 39 11                        cmp qword ptr [rcx], rdx
004961D3  74 07                           je 0x1404961dc
004961D5  B9 03 00 00 00                  mov ecx, 3
004961DA  CD 29                           int 0x29
004961DC  48 89 13                        mov qword ptr [rbx], rdx
004961DF  8A D0                           mov dl, al
004961E1  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
004961E5  48 89 19                        mov qword ptr [rcx], rbx
004961E8  48 8D 0D 59 61 AF 00            lea rcx, [rip + 0xaf6159]
004961EF  FF 05 1B 61 AF 00               inc dword ptr [rip + 0xaf611b]
004961F5  48 89 1D 0C 61 AF 00            mov qword ptr [rip + 0xaf610c], rbx
004961FC  E8 9F C9 EF FF                  call 0x140392ba0
00496201  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00496206  8B C7                           mov eax, edi
00496208  48 83 C4 20                     add rsp, 0x20
0049620C  5F                              pop rdi
0049620D  C3                              ret
0049620E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpDeviceCompletionQueueAddDispatchedRequest(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11493787, a2, a3, a4);
    v_rdi = 0;
    v_rdi = ((*(unsigned __int64 *)(v_rip + 11493684)) == (v_rip + 11493693)) ? 1 : 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11493708))) != (v_rip + 11493693)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a2) = v_rip + 11493693;
    *(unsigned __int64 *)(a2 + 8) = a1;
    *(unsigned __int64 *)(a1) = a2;
    *(unsigned __int64 *)(v_rip + 11493644) = a2;
    result = KeReleaseSpinLock(v_rip + 11493721, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rdi));
}
```

## 5. (Beta) C Style

```c
int64_t PnpDeviceCompletionQueueAddDispatchedRequest(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11493787, Arg2, a3, a4);
    local_rdi = 0;
    local_rdi = ((*(uint64_t *)(v_rip + 0xAF6134)) == (v_rip + 11493693)) ? 1 : 0;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF614C))) != (v_rip + 11493693)) {
        Arg1 = 3;
    }
    *(uint64_t *)(arg2) = v_rip + 11493693;
    *(uint64_t *)(arg2 + 0x8) = Arg1;
    *(void **)(Arg1) = Arg2;
    *(void **)(v_rip + 0xAF610C) = Arg2;
    result = KeReleaseSpinLock(v_rip + 11493721, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rdi));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049619C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049619C[BB_0049619C]
  bb_004961D5[BB_004961D5]
  bb_004961DC[BB_004961DC]
  bb_0049620E[BB_0049620E]
  bb_0049619C -->|branch| bb_004961DC
  bb_0049619C -->|fallthrough| bb_004961D5
  bb_004961D5 -->|flow| bb_004961DC
```
