# ExpHpGCTimerCallback

- RVA: `0x003A3040`–`0x003A30A2` (길이 `98` bytes)
- VA: `0x00000001403A3040`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `27`개 명령, `98/98` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x003A3075` → [Feature_Servicing_LowPriPoolGC__private_IsEnabledNoReportingNoInline](../4F/Feature_Servicing_LowPriPoolGC__private_IsEnabledNoReportingNoInline_function_004F4F18.md) (function, `0x004F4F18`)
- `0x003A3080` → [ExpSelectGCWorkQueue](../4F/ExpSelectGCWorkQueue_function_004F4D78.md) (function, `0x004F4D78`)
- `0x003A308A` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [KiExpireTimer2](KiExpireTimer2_function_003A24E0.md) at `0x003A271F`

### Static image references
- `0x003A304D` → RVA `0x00EFA800` (`.data`; read)
- `0x003A3054` → RVA `0x00EFA7E0` (`.data`; read)
- `0x003A3062` → RVA `0x00491150` (`ExpHpCompactionRoutine`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A3040  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003A3045  57                              push rdi
003A3046  48 83 EC 20                     sub rsp, 0x20
003A304A  83 FA 01                        cmp edx, 1
003A304D  48 8D 05 AC 77 B5 00            lea rax, [rip + 0xb577ac]
003A3054  48 8D 1D 85 77 B5 00            lea rbx, [rip + 0xb57785]
003A305B  48 8B FA                        mov rdi, rdx
003A305E  48 0F 45 D8                     cmovne rbx, rax
003A3062  48 8D 05 E7 E0 0E 00            lea rax, [rip + 0xee0e7]
003A3069  48 83 23 00                     and qword ptr [rbx], 0
003A306D  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
003A3071  48 89 53 18                     mov qword ptr [rbx + 0x18], rdx
003A3075  E8 9E 1E 15 00                  call 0x1404f4f18
003A307A  85 C0                           test eax, eax
003A307C  74 1D                           je 0x1403a309b
003A307E  8B CF                           mov ecx, edi
003A3080  E8 F3 1C 15 00                  call 0x1404f4d78
003A3085  8B D0                           mov edx, eax
003A3087  48 8B CB                        mov rcx, rbx
003A308A  E8 91 64 F5 FF                  call 0x1402f9520
003A308F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003A3094  48 83 C4 20                     add rsp, 0x20
003A3098  5F                              pop rdi
003A3099  C3                              ret
003A309A  CC                              int3
003A309B  B8 03 00 00 00                  mov eax, 3
003A30A0  EB E3                           jmp 0x1403a3085
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpHpGCTimerCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rbx = v_rip + 11892613;
    if (((unsigned int)(a2)) != 1) { v_rbx = v_rip + 11892652; }
    *(unsigned __int64 *)(v_rbx + 16) = v_rip + 975079;
    *(unsigned __int64 *)(v_rbx + 24) = a2;
    result = Feature_Servicing_LowPriPoolGC__private_IsEnabledNoReportingNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_003A309B;
    result = ExpSelectGCWorkQueue((unsigned int)((unsigned int)(a2)), a2, a3, a4);
loc_003A3085:
    result = ExQueueWorkItem(v_rbx, (unsigned int)((unsigned int)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_003A309B:
    goto loc_003A3085;
}
```

## 5. (Beta) C Style

```c
int64_t ExpHpGCTimerCallback(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rbx = v_rip + 11892613;
    if (((uint32_t)(Arg2)) != 1) { local_rbx = v_rip + 11892652; }
    *(uint64_t *)(local_rbx + 0x10) = v_rip + 975079;
    *(uint64_t *)(local_rbx + 0x18) = Arg2;
    result = Feature_Servicing_LowPriPoolGC__private_IsEnabledNoReportingNoInline(Arg1, Arg2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_003A309B;
    result = ExpSelectGCWorkQueue((uint32_t)((uint32_t)(Arg2)), Arg2, a3, a4);
loc_003A3085:
    result = ExQueueWorkItem(local_rbx, (uint32_t)((uint32_t)(result)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_003A309B:
    goto loc_003A3085;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A3040&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A3040[BB_003A3040]
  bb_003A307E[BB_003A307E]
  bb_003A3085[BB_003A3085]
  bb_003A309A[BB_003A309A]
  bb_003A309B[BB_003A309B]
  bb_003A3040 -->|branch| bb_003A309B
  bb_003A3040 -->|fallthrough| bb_003A307E
  bb_003A307E -->|flow| bb_003A3085
  bb_003A309A -->|flow| bb_003A309B
  bb_003A309B -->|branch| bb_003A3085
```
