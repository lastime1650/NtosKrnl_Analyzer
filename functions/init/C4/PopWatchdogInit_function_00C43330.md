# PopWatchdogInit

- RVA: `0x00C43330`–`0x00C43420` (길이 `240` bytes)
- VA: `0x0000000140C43330`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `44`개 명령, `240/240` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **26**

### Outgoing calls
- `0x00C43354` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00C433D2` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00C433E7` → [KeInitializeTriageDumpDataArray](../../text/4B/KeInitializeTriageDumpDataArray_function_004BA020.md) (function, `0x004BA020`)
- `0x00C43409` → [KeRegisterBugCheckReasonCallback](../../text/47/KeRegisterBugCheckReasonCallback_function_004720A0.md) (function, `0x004720A0`)

### Direct callers
- [PoInitSystem](../C7/PoInitSystem_function_00C72358.md) at `0x00C72D50`

### Static image references
- `0x00C43336` → RVA `0x00F08400` (`.data`; read)
- `0x00C4333F` → RVA `0x00F08408` (`.data`; write)
- `0x00C43346` → RVA `0x00F08400` (`.data`; write)
- `0x00C4334D` → RVA `0x00F083F8` (`.data`; write)
- `0x00C43359` → RVA `0x00F0BEB8` (`.data`; read)
- `0x00C43360` → RVA `0x00F0BEB0` (`.data`; write)
- `0x00C43367` → RVA `0x00F0BEC0` (`.data`; write)
- `0x00C4336E` → RVA `0x00F0BEB8` (`.data`; write)
- `0x00C43375` → RVA `0x005D51A0` (`PopPowerActionWatchdog`; read)
- `0x00C4337C` → RVA `0x00F0BE88` (`.data`; write)
- `0x00C43383` → RVA `0x00F0C9B8` (`.data`; write)
- `0x00C4338A` → RVA `0x00F0BE68` (`.data`; write)
- `0x00C43398` → RVA `0x00F0BEC8` (`.data`; write)
- `0x00C4339F` → RVA `0x00F0BEEC` (`.data`; write)
- `0x00C433A5` → RVA `0x00F0BEE8` (`.data`; write)
- `0x00C433AC` → RVA `0x00F0BE70` (`.data`; write)
- `0x00C433B6` → RVA `0x00F0BE90` (`.data`; write)
- `0x00C433BD` → RVA `0x00F0BEA8` (`.data`; write)
- `0x00C433C4` → RVA `0x00F0BE80` (`.data`; write)
- `0x00C433CB` → RVA `0x00F0BEF0` (`.data`; write)
- `0x00C433DA` → RVA `0x00E01D44` (`.data`; write)
- `0x00C433E0` → RVA `0x00E01D48` (`.data`; read)
- `0x00C433F0` → RVA `0x00E01D10` (`.data`; read)
- `0x00C433FB` → RVA `0x00E01D08` (`.data`; read)
- `0x00C43402` → RVA `0x00E01D18` (`.data`; read)
- `0x00C43412` → RVA `0x00E01D00` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00C43354` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`INIT` → `PAGELK`)
  - `0x00C433D2` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`INIT` → `PAGELK`)
  - `0x00C433E7` → [KeInitializeTriageDumpDataArray](../../text/4B/KeInitializeTriageDumpDataArray_function_004BA020.md) (`INIT` → `.text`)
  - `0x00C43409` → [KeRegisterBugCheckReasonCallback](../../text/47/KeRegisterBugCheckReasonCallback_function_004720A0.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C43330  40 53                           push rbx
00C43332  48 83 EC 20                     sub rsp, 0x20
00C43336  48 8D 05 C3 50 2C 00            lea rax, [rip + 0x2c50c3]
00C4333D  33 DB                           xor ebx, ebx
00C4333F  48 89 05 C2 50 2C 00            mov qword ptr [rip + 0x2c50c2], rax
00C43346  48 89 05 B3 50 2C 00            mov qword ptr [rip + 0x2c50b3], rax
00C4334D  48 89 1D A4 50 2C 00            mov qword ptr [rip + 0x2c50a4], rbx
00C43354  E8 67 50 F3 FF                  call 0x140b783c0
00C43359  48 8D 05 58 8B 2C 00            lea rax, [rip + 0x2c8b58]
00C43360  48 89 1D 49 8B 2C 00            mov qword ptr [rip + 0x2c8b49], rbx
00C43367  48 89 05 52 8B 2C 00            mov qword ptr [rip + 0x2c8b52], rax
00C4336E  48 89 05 43 8B 2C 00            mov qword ptr [rip + 0x2c8b43], rax
00C43375  48 8D 05 24 1E 99 FF            lea rax, [rip - 0x66e1dc]
00C4337C  48 89 05 05 8B 2C 00            mov qword ptr [rip + 0x2c8b05], rax
00C43383  48 89 1D 2E 96 2C 00            mov qword ptr [rip + 0x2c962e], rbx
00C4338A  48 89 1D D7 8A 2C 00            mov qword ptr [rip + 0x2c8ad7], rbx
00C43391  C6 05 18 8B 2C 00 08            mov byte ptr [rip + 0x2c8b18], 8
00C43398  48 89 1D 29 8B 2C 00            mov qword ptr [rip + 0x2c8b29], rbx
00C4339F  89 1D 47 8B 2C 00               mov dword ptr [rip + 0x2c8b47], ebx
00C433A5  66 89 1D 3C 8B 2C 00            mov word ptr [rip + 0x2c8b3c], bx
00C433AC  C7 05 BA 8A 2C 00 13 01 00 00   mov dword ptr [rip + 0x2c8aba], 0x113
00C433B6  48 89 1D D3 8A 2C 00            mov qword ptr [rip + 0x2c8ad3], rbx
00C433BD  48 89 1D E4 8A 2C 00            mov qword ptr [rip + 0x2c8ae4], rbx
00C433C4  48 89 1D B5 8A 2C 00            mov qword ptr [rip + 0x2c8ab5], rbx
00C433CB  C6 05 1E 8B 2C 00 01            mov byte ptr [rip + 0x2c8b1e], 1
00C433D2  E8 39 50 F3 FF                  call 0x140b78410
00C433D7  8D 53 40                        lea edx, [rbx + 0x40]
00C433DA  88 1D 64 E9 1B 00               mov byte ptr [rip + 0x1be964], bl
00C433E0  48 8D 0D 61 E9 1B 00            lea rcx, [rip + 0x1be961]
00C433E7  E8 34 6C 87 FF                  call 0x1404ba020
00C433EC  85 C0                           test eax, eax
00C433EE  78 29                           js 0x140c43419
00C433F0  4C 8B 0D 19 E9 1B 00            mov r9, qword ptr [rip + 0x1be919]
00C433F7  44 8D 43 07                     lea r8d, [rbx + 7]
00C433FB  48 8B 15 06 E9 1B 00            mov rdx, qword ptr [rip + 0x1be906]
00C43402  48 8D 0D 0F E9 1B 00            lea rcx, [rip + 0x1be90f]
00C43409  E8 92 EC 82 FF                  call 0x1404720a0
00C4340E  84 C0                           test al, al
00C43410  74 07                           je 0x140c43419
00C43412  C6 05 E7 E8 1B 00 01            mov byte ptr [rip + 0x1be8e7], 1
00C43419  48 83 C4 20                     add rsp, 0x20
00C4341D  5B                              pop rbx
00C4341E  C3                              ret
00C4341F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopWatchdogInit(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    *(unsigned __int64 *)(v_rip + 2904258) = v_rip + 2904259;
    *(unsigned __int64 *)(v_rip + 2904243) = v_rip + 2904259;
    *(unsigned __int64 *)(v_rip + 2904228) = 0;
    result = PopAcquirePolicyLock(a1, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 2919241) = 0;
    *(unsigned __int64 *)(v_rip + 2919250) = v_rip + 2919256;
    *(unsigned __int64 *)(v_rip + 2919235) = v_rip + 2919256;
    *(unsigned __int64 *)(v_rip + 2919173) = v_rip - 6742492;
    *(unsigned __int64 *)(v_rip + 2922030) = 0;
    *(unsigned __int64 *)(v_rip + 2919127) = 0;
    *(unsigned __int8 *)(v_rip + 2919192) = 8;
    *(unsigned __int64 *)(v_rip + 2919209) = 0;
    *(unsigned int *)(v_rip + 2919239) = 0;
    *(unsigned __int16 *)(v_rip + 2919228) = 0;
    *(unsigned int *)(v_rip + 2919098) = 275;
    *(unsigned __int64 *)(v_rip + 2919123) = 0;
    *(unsigned __int64 *)(v_rip + 2919140) = 0;
    *(unsigned __int64 *)(v_rip + 2919093) = 0;
    *(unsigned __int8 *)(v_rip + 2919198) = 1;
    result = PopReleasePolicyLock(a1, a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 1829220) = 0;
    result = KeInitializeTriageDumpDataArray(v_rip + 1829217, v_rbx + 64, a3, a4);
    if (sign_flag) goto loc_00C43419;
    result = KeRegisterBugCheckReasonCallback(v_rip + 1829135, *(unsigned __int64 *)(v_rip + 1829126), v_rbx + 7, *(unsigned __int64 *)(v_rip + 1829145));
    if ((unsigned __int8)(result) != 0) {
        *(unsigned __int8 *)(v_rip + 1829095) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopWatchdogInit(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    *(uint64_t *)(v_rip + 0x2C50C2) = v_rip + 2904259;
    *(uint64_t *)(v_rip + 0x2C50B3) = v_rip + 2904259;
    *(uint64_t *)(v_rip + 0x2C50A4) = 0;
    result = PopAcquirePolicyLock(a1, a2, a3, a4);
    *(uint64_t *)(v_rip + 0x2C8B49) = 0;
    *(uint64_t *)(v_rip + 0x2C8B52) = v_rip + 2919256;
    *(uint64_t *)(v_rip + 0x2C8B43) = v_rip + 2919256;
    *(uint64_t *)(v_rip + 0x2C8B05) = v_rip - 6742492;
    *(uint64_t *)(v_rip + 0x2C962E) = 0;
    *(uint64_t *)(v_rip + 0x2C8AD7) = 0;
    *(uint8_t *)(v_rip + 0x2C8B18) = 8;
    *(uint64_t *)(v_rip + 0x2C8B29) = 0;
    *(uint32_t *)(v_rip + 0x2C8B47) = 0;
    *(uint16_t *)(v_rip + 0x2C8B3C) = 0;
    *(uint32_t *)(v_rip + 0x2C8ABA) = 275;
    *(uint64_t *)(v_rip + 0x2C8AD3) = 0;
    *(uint64_t *)(v_rip + 0x2C8AE4) = 0;
    *(uint64_t *)(v_rip + 0x2C8AB5) = 0;
    *(uint8_t *)(v_rip + 0x2C8B1E) = 1;
    result = PopReleasePolicyLock(a1, a2, a3, a4);
    *(uint8_t *)(v_rip + 0x1BE964) = 0;
    result = KeInitializeTriageDumpDataArray(v_rip + 1829217, local_rbx + 64, a3, a4);
    if (sign_flag) goto loc_00C43419;
    result = KeRegisterBugCheckReasonCallback(v_rip + 1829135, *(uint64_t *)(v_rip + 0x1BE906), local_rbx + 7, *(uint64_t *)(v_rip + 0x1BE919));
    if ((uint8_t)(result) != 0) {
        *(uint8_t *)(v_rip + 0x1BE8E7) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C43330&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C43330[BB_00C43330]
  bb_00C433F0[BB_00C433F0]
  bb_00C43412[BB_00C43412]
  bb_00C43419[BB_00C43419]
  bb_00C4341F[BB_00C4341F]
  bb_00C43330 -->|branch| bb_00C43419
  bb_00C43330 -->|fallthrough| bb_00C433F0
  bb_00C433F0 -->|branch| bb_00C43419
  bb_00C433F0 -->|fallthrough| bb_00C43412
  bb_00C43412 -->|flow| bb_00C43419
```
