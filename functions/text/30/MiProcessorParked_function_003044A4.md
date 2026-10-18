# MiProcessorParked

- RVA: `0x003044A4`–`0x00304508` (길이 `100` bytes)
- VA: `0x00000001403044A4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000684A0`
- 디코드: `26`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x003044C3` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x003044D8` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)

### Direct callers
- [MiMoveBackgroundZeroThreads](MiMoveBackgroundZeroThreads_function_00305810.md) at `0x00305A2D`

### Static image references
- `0x003044BA` → RVA `0x00E2ED40` (`.data`; read)
- `0x003044C8` → RVA `0x00E2ED48` (`.data`; read)
- `0x003044F3` → RVA `0x00E2ED50` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003044A4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003044A9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
003044AE  57                              push rdi
003044AF  48 83 EC 20                     sub rsp, 0x20
003044B3  0F B7 71 08                     movzx esi, word ptr [rcx + 8]
003044B7  48 8B F9                        mov rdi, rcx
003044BA  48 8D 0D 7F A8 B2 00            lea rcx, [rip + 0xb2a87f]
003044C1  33 DB                           xor ebx, ebx
003044C3  E8 68 49 F4 FF                  call 0x140248e30
003044C8  66 3B 35 79 A8 B2 00            cmp si, word ptr [rip + 0xb2a879]
003044CF  72 1F                           jb 0x1403044f0
003044D1  48 8D 0D 68 A8 B2 00            lea rcx, [rip + 0xb2a868]
003044D8  E8 B3 60 F4 FF                  call 0x14024a590
003044DD  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003044E2  8B C3                           mov eax, ebx
003044E4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003044E9  48 83 C4 20                     add rsp, 0x20
003044ED  5F                              pop rdi
003044EE  C3                              ret
003044EF  CC                              int3
003044F0  4C 8B 07                        mov r8, qword ptr [rdi]
003044F3  48 8D 05 56 A8 B2 00            lea rax, [rip + 0xb2a856]
003044FA  4C 85 04 F0                     test qword ptr [rax + rsi*8], r8
003044FE  B8 01 00 00 00                  mov eax, 1
00304503  0F 45 D8                        cmovne ebx, eax
00304506  EB C9                           jmp 0x1403044d1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiProcessorParked(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    result = ExAcquireSpinLockSharedAtDpcLevel(v_rip + 11708543, a2, a3, a4);
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 8))) < (*(unsigned __int16 *)(v_rip + 11708537))) goto loc_003044F0;
loc_003044D1:
    result = ExReleaseSpinLockSharedFromDpcLevel(v_rip + 11708520, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return 0;
loc_003044F0:
    v_rbx = v_stack_p8;
    if (((*(unsigned __int64 *)(v_rip + 11708502 + v_stack_p10 * 8)) & (*(unsigned __int64 *)(a1))) != 0) { v_rbx = 1; }
    goto loc_003044D1;
}
```

## 5. (Beta) C Style

```c
int64_t MiProcessorParked(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    result = ExAcquireSpinLockSharedAtDpcLevel(v_rip + 11708543, a2, a3, a4);
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x8))) < (*(uint16_t *)(v_rip + 0xB2A879))) goto loc_003044F0;
loc_003044D1:
    result = ExReleaseSpinLockSharedFromDpcLevel(v_rip + 11708520, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return 0;
loc_003044F0:
    local_rbx = v_stack_p8;
    if (((*(uint64_t *)(v_rip + 0xB2A856 + v_stack_p10 * 8)) & (*(uint64_t *)(arg1))) != 0) { local_rbx = 1; }
    goto loc_003044D1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003044A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003044A4[BB_003044A4]
  bb_003044D1[BB_003044D1]
  bb_003044EF[BB_003044EF]
  bb_003044F0[BB_003044F0]
  bb_003044A4 -->|branch| bb_003044F0
  bb_003044A4 -->|fallthrough| bb_003044D1
  bb_003044EF -->|flow| bb_003044F0
  bb_003044F0 -->|branch| bb_003044D1
```
