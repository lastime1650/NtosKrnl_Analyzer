# PopPowerButtonTimerCallback

- RVA: `0x005D9A00`–`0x005D9A5E` (길이 `94` bytes)
- VA: `0x00000001405D9A00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `24`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x005D9A10` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x005D9A46` → [PopQueueWorkItem](../4A/PopQueueWorkItem_function_004A20F8.md) (function, `0x004A20F8`)
- `0x005D9A52` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005D9A06` → RVA `0x00F08600` (`.data`; read)
- `0x005D9A15` → RVA `0x00F086B8` (`.data`; read)
- `0x005D9A24` → RVA `0x00F086BC` (`.data`; read)
- `0x005D9A2F` → RVA `0x00F08690` (`.data`; read)
- `0x005D9A40` → RVA `0x00F086B8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D9A00  40 53                           push rbx
005D9A02  48 83 EC 20                     sub rsp, 0x20
005D9A06  48 8D 0D F3 EB 92 00            lea rcx, [rip + 0x92ebf3]
005D9A0D  48 8B DA                        mov rbx, rdx
005D9A10  E8 1B EA C2 FF                  call 0x140208430
005D9A15  8B 05 9D EC 92 00               mov eax, dword ptr [rip + 0x92ec9d]
005D9A1B  44 8B C0                        mov r8d, eax
005D9A1E  41 83 E0 01                     and r8d, 1
005D9A22  74 27                           je 0x1405d9a4b
005D9A24  39 1D 92 EC 92 00               cmp dword ptr [rip + 0x92ec92], ebx
005D9A2A  75 1F                           jne 0x1405d9a4b
005D9A2C  83 E0 FE                        and eax, 0xfffffffe
005D9A2F  48 8D 0D 5A EC 92 00            lea rcx, [rip + 0x92ec5a]
005D9A36  05 D0 07 00 00                  add eax, 0x7d0
005D9A3B  33 D2                           xor edx, edx
005D9A3D  41 0B C0                        or eax, r8d
005D9A40  89 05 72 EC 92 00               mov dword ptr [rip + 0x92ec72], eax
005D9A46  E8 AD 86 EC FF                  call 0x1404a20f8
005D9A4B  48 8D 0D AE EB 92 00            lea rcx, [rip + 0x92ebae]
005D9A52  E8 19 CC C2 FF                  call 0x140206670
005D9A57  48 83 C4 20                     add rsp, 0x20
005D9A5B  5B                              pop rbx
005D9A5C  C3                              ret
005D9A5D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerButtonTimerCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 9628659, a2, a3, a4);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9628829))))) & (1));
    if (condition_is_equal) goto loc_005D9A4B;
    result = (unsigned int)(*(unsigned int *)(v_rip + 9628829));
    if ((*(unsigned int *)(v_rip + 9628818)) == ((unsigned int)(a2))) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9628829))) & (0xFFFFFFFEULL));
        a1 = v_rip + 9628762;
        result = (unsigned int)((result) + (0x7D0ULL));
        a2 = 0;
        result = (unsigned int)((result) | ((unsigned int)(a3)));
        *(unsigned int *)(v_rip + 9628786) = (unsigned int)(result);
        result = PopQueueWorkItem(a1, a2, a3, a4);
    }
    result = KxReleaseSpinLock(v_rip + 9628590, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerButtonTimerCallback(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 9628659, Arg2, a3, a4);
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x92EC9D))))) & (1));
    if (condition_is_equal) goto loc_005D9A4B;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x92EC9D));
    if ((*(uint32_t *)(v_rip + 0x92EC92)) == ((uint32_t)(Arg2))) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x92EC9D))) & (0xFFFFFFFEULL));
        Arg1 = v_rip + 9628762;
        result = (uint32_t)((result) + (0x7D0ULL));
        Arg2 = 0;
        result = (uint32_t)((result) | ((uint32_t)(a3)));
        *(uint32_t *)(v_rip + 0x92EC72) = (uint32_t)(result);
        result = PopQueueWorkItem(Arg1, Arg2, a3, a4);
    }
    result = KxReleaseSpinLock(v_rip + 9628590, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D9A00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D9A00[BB_005D9A00]
  bb_005D9A24[BB_005D9A24]
  bb_005D9A2C[BB_005D9A2C]
  bb_005D9A4B[BB_005D9A4B]
  bb_005D9A5D[BB_005D9A5D]
  bb_005D9A00 -->|branch| bb_005D9A4B
  bb_005D9A00 -->|fallthrough| bb_005D9A24
  bb_005D9A24 -->|branch| bb_005D9A4B
  bb_005D9A24 -->|fallthrough| bb_005D9A2C
  bb_005D9A2C -->|flow| bb_005D9A4B
```
