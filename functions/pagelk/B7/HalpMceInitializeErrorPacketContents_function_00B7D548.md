# HalpMceInitializeErrorPacketContents

- RVA: `0x00B7D548`–`0x00B7D5AB` (길이 `99` bytes)
- VA: `0x0000000140B7D548`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `22`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B7D559` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [HalpHandlePreviousMcaErrors](../B5/HalpHandlePreviousMcaErrors_function_00B5B8E4.md) at `0x00B5B942`
- [HalpHandlePreviousMcaErrorsOnProcessor](../B5/HalpHandlePreviousMcaErrorsOnProcessor_function_00B5BA2C.md) at `0x00B5BA86`
- [HalpMceInitializeErrorPacket](HalpMceInitializeErrorPacket_function_00B7D4BC.md) at `0x00B7D50C`

### Static image references
- `0x00B7D55E` → RVA `0x00E100E4` (`.data`; read)
- `0x00B7D564` → RVA `0x0001E948` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B7D559` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B7D548  40 53                           push rbx
00B7D54A  48 83 EC 20                     sub rsp, 0x20
00B7D54E  33 D2                           xor edx, edx
00B7D550  41 B8 F8 04 00 00               mov r8d, 0x4f8
00B7D556  48 8B D9                        mov rbx, rcx
00B7D559  E8 E2 96 B4 FF                  call 0x1406c6c40
00B7D55E  8B 05 80 2B 29 00               mov eax, dword ptr [rip + 0x292b80]
00B7D564  0F 10 05 DD 13 4A FF            movups xmm0, xmmword ptr [rip - 0xb5ec23]
00B7D56B  89 43 18                        mov dword ptr [rbx + 0x18], eax
00B7D56E  48 8D 43 50                     lea rax, [rbx + 0x50]
00B7D572  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
00B7D576  F3 0F 7F 43 20                  movdqu xmmword ptr [rbx + 0x20], xmm0
00B7D57B  C7 03 57 48 45 41               mov dword ptr [rbx], 0x41454857
00B7D581  C7 43 04 03 00 00 00            mov dword ptr [rbx + 4], 3
00B7D588  C7 43 08 F8 04 00 00            mov dword ptr [rbx + 8], 0x4f8
00B7D58F  C7 43 38 01 00 00 00            mov dword ptr [rbx + 0x38], 1
00B7D596  C7 43 40 50 00 00 00            mov dword ptr [rbx + 0x40], 0x50
00B7D59D  C7 43 44 A8 04 00 00            mov dword ptr [rbx + 0x44], 0x4a8
00B7D5A4  48 83 C4 20                     add rsp, 0x20
00B7D5A8  5B                              pop rbx
00B7D5A9  C3                              ret
00B7D5AA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpMceInitializeErrorPacketContents(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = memset(a1, a2, (unsigned int)(0x4F8ULL), a4);
    *(unsigned int *)(a1 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2698112)));
    *(unsigned __int64 *)(a1 + 48) = a1 + 80;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned int *)(a1) = 0x41454857ULL;
    *(unsigned int *)(a1 + 4) = 3;
    *(unsigned int *)(a1 + 8) = 0x4F8ULL;
    *(unsigned int *)(a1 + 56) = 1;
    *(unsigned int *)(a1 + 64) = 80;
    *(unsigned int *)(a1 + 68) = 0x4A8ULL;
    v_rsp = (v_rsp) + (32);
    return a1 + 80;
}
```

## 5. (Beta) C Style

```c
void *HalpMceInitializeErrorPacketContents(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = memset(Arg1, Arg2, (uint32_t)(0x4F8ULL), a4);
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x292B80)));
    *(void **)(arg1 + 0x30) = Arg1 + 80;
    *(uint64_t *)(arg1 + 0x20) = v_xmm0;
    *(uint32_t *)(arg1) = 0x41454857ULL;
    *(uint32_t *)(arg1 + 0x4) = 3;
    *(uint32_t *)(arg1 + 0x8) = 0x4F8ULL;
    *(uint32_t *)(arg1 + 0x38) = 1;
    *(uint32_t *)(arg1 + 0x40) = 80;
    *(uint32_t *)(arg1 + 0x44) = 0x4A8ULL;
    local_rsp = (local_rsp) + (32);
    return Arg1 + 80;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x20` | `128` | `W` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x40` | `32` | `W` |
| `Arg1` | `+ 0x44` | `32` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B7D548&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B7D548[BB_00B7D548]
  bb_00B7D5AA[BB_00B7D5AA]
```
