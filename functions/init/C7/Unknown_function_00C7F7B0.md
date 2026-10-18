# sub_00C7F7B0

- RVA: `0x00C7F7B0`–`0x00C7F848` (길이 `152` bytes)
- VA: `0x0000000140C7F7B0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF4C0`
- 디코드: `38`개 명령, `152/152` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C7F82D` → [KeExpandKernelStackAndCallout](../../text/46/KeExpandKernelStackAndCallout_function_004675F0.md) (function, `0x004675F0`)
- `0x00C7F83B` → [KdEnableDebugger](../../text/5B/KdEnableDebugger_function_005B0A40.md) (function, `0x005B0A40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C7F826` → RVA `0x00C18CA0` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C7F82D` → [KeExpandKernelStackAndCallout](../../text/46/KeExpandKernelStackAndCallout_function_004675F0.md) (`INIT` → `.text`)
  - `0x00C7F83B` → [KdEnableDebugger](../../text/5B/KdEnableDebugger_function_005B0A40.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C7F7B0  40 55                           push rbp
00C7F7B2  48 83 EC 30                     sub rsp, 0x30
00C7F7B6  48 8B EA                        mov rbp, rdx
00C7F7B9  48 8B 6D 78                     mov rbp, qword ptr [rbp + 0x78]
00C7F7BD  0F 31                           rdtsc
00C7F7BF  48 C1 E2 20                     shl rdx, 0x20
00C7F7C3  48 0B C2                        or rax, rdx
00C7F7C6  48 8B D0                        mov rdx, rax
00C7F7C9  48 8B C8                        mov rcx, rax
00C7F7CC  48 C1 C9 03                     ror rcx, 3
00C7F7D0  48 33 D1                        xor rdx, rcx
00C7F7D3  48 B8 01 20 00 04 80 00 10 70   movabs rax, 0x7010008004002001
00C7F7DD  48 F7 E2                        mul rdx
00C7F7E0  48 8B CA                        mov rcx, rdx
00C7F7E3  48 33 C8                        xor rcx, rax
00C7F7E6  48 B8 C5 4E EC C4 4E EC C4 4E   movabs rax, 0x4ec4ec4ec4ec4ec5
00C7F7F0  48 F7 E1                        mul rcx
00C7F7F3  48 C1 EA 02                     shr rdx, 2
00C7F7F7  48 6B C2 0D                     imul rax, rdx, 0xd
00C7F7FB  48 2B C8                        sub rcx, rax
00C7F7FE  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
00C7F801  83 65 4C 00                     and dword ptr [rbp + 0x4c], 0
00C7F805  C7 45 50 01 00 00 00            mov dword ptr [rbp + 0x50], 1
00C7F80C  48 83 65 58 00                  and qword ptr [rbp + 0x58], 0
00C7F811  C7 45 60 02 00 00 00            mov dword ptr [rbp + 0x60], 2
00C7F818  C6 45 64 00                     mov byte ptr [rbp + 0x64], 0
00C7F81C  41 B8 00 C0 00 00               mov r8d, 0xc000
00C7F822  48 8D 55 48                     lea rdx, [rbp + 0x48]
00C7F826  48 8D 0D 73 94 F9 FF            lea rcx, [rip - 0x66b8d]
00C7F82D  E8 BE 7D 7E FF                  call 0x1404675f0
00C7F832  83 BD A4 00 00 00 00            cmp dword ptr [rbp + 0xa4], 0
00C7F839  7C 06                           jl 0x140c7f841
00C7F83B  E8 00 12 93 FF                  call 0x1405b0a40
00C7F840  90                              nop
00C7F841  48 83 C4 30                     add rsp, 0x30
00C7F845  5D                              pop rbp
00C7F846  C3                              ret
00C7F847  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00C7F7B0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    a1 = (a2) ^ (result);
    a2 = (a2) >> (2);
    result = (result) * (a2);
    a1 = (a1) - (result);
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 120) + 72) = (unsigned int)(a1);
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 120) + 80) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 120) + 96) = 2;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 120) + 100) = 0;
    result = KeExpandKernelStackAndCallout(v_rip - 420749, *(unsigned __int64 *)(a2 + 120) + 72, (unsigned int)(0xC000ULL), a4);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 120) + 164)) >= 0) {
        result = KdEnableDebugger(v_rip - 420749, *(unsigned __int64 *)(a2 + 120) + 72, (unsigned int)(0xC000ULL), a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00C7F7B0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    Arg1 = (Arg2) ^ (result);
    Arg2 = (Arg2) >> (2);
    result = (result) * (Arg2);
    Arg1 = (Arg1) - (result);
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x78) + 0x48) = (uint32_t)(Arg1);
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x78) + 0x50) = 1;
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x78) + 0x60) = 2;
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x78) + 0x64) = 0;
    result = KeExpandKernelStackAndCallout(v_rip - 420749, *(uint64_t *)(arg2 + 0x78) + 72, (uint32_t)(0xC000ULL), a4);
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x78) + 0xA4)) >= 0) {
        result = KdEnableDebugger(v_rip - 420749, *(uint64_t *)(arg2 + 0x78) + 72, (uint32_t)(0xC000ULL), a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x78` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C7F7B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C7F7B0[BB_00C7F7B0]
  bb_00C7F83B[BB_00C7F83B]
  bb_00C7F841[BB_00C7F841]
  bb_00C7F847[BB_00C7F847]
  bb_00C7F7B0 -->|branch| bb_00C7F841
  bb_00C7F7B0 -->|fallthrough| bb_00C7F83B
  bb_00C7F83B -->|flow| bb_00C7F841
```
