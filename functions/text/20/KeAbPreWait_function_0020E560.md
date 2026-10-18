# KeAbPreWait

- RVA: `0x0020E560`–`0x0020E596` (길이 `54` bytes)
- VA: `0x000000014020E560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DAC8`
- 디코드: `22`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **21**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0020E58F` → [KiAbEntryRemoveFromTree](../26/KiAbEntryRemoveFromTree_function_00262410.md) (function, `0x00262410`)

### Direct callers
- [sub_0020D8DF](Unknown_function_0020D8DF.md) at `0x0020DB4E`
- [sub_0020DEED](Unknown_function_0020DEED.md) at `0x0020DF18`
- [sub_0020E5E6](Unknown_function_0020E5E6.md) at `0x0020E611`
- [ExfAcquirePushLockExclusiveEx](ExfAcquirePushLockExclusiveEx_function_0020FC90.md) at `0x0020FF21`
- [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) at `0x002104FC`
- [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) at `0x0021054B`
- [MiReferenceControlArea](../2B/MiReferenceControlArea_function_002BC198.md) at `0x002BC41A`
- [MiLockControlAreaSectionExtend](../2C/MiLockControlAreaSectionExtend_function_002C9D60.md) at `0x002C9E59`
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x0033FC66`
- [sub_0034FCFA](../34/Unknown_function_0034FCFA.md) at `0x0034FD35`
- [MiWaitForCollidedFaultComplete](../36/MiWaitForCollidedFaultComplete_function_00369EDC.md) at `0x0036A127`
- [sub_003F374F](../3F/Unknown_function_003F374F.md) at `0x003F3783`
- [sub_00415140](../41/Unknown_function_00415140.md) at `0x00415173`
- [ExpAcquireFastMutexContended](../45/ExpAcquireFastMutexContended_function_00450288.md) at `0x004502C4`
- [MiChangingSubsectionProtos](../68/MiChangingSubsectionProtos_function_0068057C.md) at `0x00680684`
- [MiWaitForExtentDeletions](../68/MiWaitForExtentDeletions_function_00681F80.md) at `0x00681FB5`
- [sub_006D969C](../6D/Unknown_function_006D969C.md) at `0x006D9848`
- [sub_006E8106](../6E/Unknown_function_006E8106.md) at `0x006E8132`
- [IopWaitAndAcquireFileObjectLock](../../page/8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) at `0x008AE712`
- [VrpWaitForDiffHiveEntryTransitionOwnerToLeave](../../page/93/VrpWaitForDiffHiveEntryTransitionOwnerToLeave_function_00937128.md) at `0x009371A7`
- [CmpWaitOnHiveWriteQueue](../../page/AA/CmpWaitOnHiveWriteQueue_function_00AA0110.md) at `0x00AA01CD`
- [PfpPrefetchSharedConflictNotifyStart](../../page/AB/PfpPrefetchSharedConflictNotifyStart_function_00ABC350.md) at `0x00ABC3CD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0020E560  40 53                           push rbx
0020E562  48 83 EC 20                     sub rsp, 0x20
0020E566  0F B6 01                        movzx eax, byte ptr [rcx]
0020E569  48 8B D9                        mov rbx, rcx
0020E56C  0C 02                           or al, 2
0020E56E  88 01                           mov byte ptr [rcx], al
0020E570  90                              nop
0020E571  48 8B 01                        mov rax, qword ptr [rcx]
0020E574  48 C1 E8 3F                     shr rax, 0x3f
0020E578  84 C0                           test al, al
0020E57A  75 13                           jne 0x14020e58f
0020E57C  C6 43 09 01                     mov byte ptr [rbx + 9], 1
0020E580  90                              nop
0020E581  0F B6 03                        movzx eax, byte ptr [rbx]
0020E584  24 FD                           and al, 0xfd
0020E586  88 03                           mov byte ptr [rbx], al
0020E588  48 83 C4 20                     add rsp, 0x20
0020E58C  5B                              pop rbx
0020E58D  C3                              ret
0020E58E  CC                              int3
0020E58F  E8 7C 3E 05 00                  call 0x140262410
0020E594  EB E6                           jmp 0x14020e57c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeAbPreWait(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned __int8)((*(unsigned __int8 *)(a1)) | (2));
    *(unsigned __int8 *)(a1) = (unsigned __int8)(result);
    result = (*(unsigned __int64 *)(a1)) >> (63);
    if ((unsigned __int8)(result) != 0) goto loc_0020E58F;
loc_0020E57C:
    *(unsigned __int8 *)(a1 + 9) = 1;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1)) & (253));
    *(unsigned __int8 *)(a1) = (unsigned __int8)(result);
    v_rsp = (v_rsp) + (32);
    return result;
loc_0020E58F:
    result = KiAbEntryRemoveFromTree(a1, a2, a3, a4);
    goto loc_0020E57C;
}
```

## 5. (Beta) C Style

```c
int64_t KeAbPreWait(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint8_t)((*(uint8_t *)(arg1)) | (2));
    *(uint8_t *)(arg1) = (uint8_t)(result);
    result = (*(uint64_t *)(arg1)) >> (63);
    if ((uint8_t)(result) != 0) goto loc_0020E58F;
loc_0020E57C:
    *(uint8_t *)(arg1 + 0x9) = 1;
    result = (uint8_t)((*(uint8_t *)(arg1)) & (253));
    *(uint8_t *)(arg1) = (uint8_t)(result);
    local_rsp = (local_rsp) + (32);
    return result;
loc_0020E58F:
    result = KiAbEntryRemoveFromTree(Arg1, a2, a3, a4);
    goto loc_0020E57C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `8` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x9` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020E560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0020E560[BB_0020E560]
  bb_0020E57C[BB_0020E57C]
  bb_0020E58E[BB_0020E58E]
  bb_0020E58F[BB_0020E58F]
  bb_0020E560 -->|branch| bb_0020E58F
  bb_0020E560 -->|fallthrough| bb_0020E57C
  bb_0020E58E -->|flow| bb_0020E58F
  bb_0020E58F -->|branch| bb_0020E57C
```
