# sub_006DEED6

- RVA: `0x006DEED6`–`0x006DEEFD` (길이 `39` bytes)
- VA: `0x00000001406DEED6`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071D78`
- 디코드: `10`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DEEE5` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x006DEEED` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x006DEEF2` → [KeLeaveGuardedRegion](../2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DEEF8` → [RtlpCSparseBitmapUnlock + 0x29](../2F/RtlpCSparseBitmapUnlock_function_002F0DD0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DEED6  B8 11 00 00 00                  mov eax, 0x11
006DEEDB  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
006DEEE0  74 08                           je 0x1406deeea
006DEEE2  48 8B CB                        mov rcx, rbx
006DEEE5  E8 56 45 B8 FF                  call 0x140263440
006DEEEA  48 8B CB                        mov rcx, rbx
006DEEED  E8 0E 27 C0 FF                  call 0x1402e1600
006DEEF2  E8 49 3D C0 FF                  call 0x1402e2c40
006DEEF7  90                              nop
006DEEF8  E9 FC 1E C1 FF                  jmp 0x1402f0df9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DEED6(__int64 a1, __int64 a2)
{
    __int64 result;

    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_rbx;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rbx, a2, a3, a4);
    result = KeLeaveGuardedRegion(v_rbx, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DEED6(int64_t Arg1, int64_t Arg2)
{
    int64_t result;

    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = local_rbx;
        result = ExfReleasePushLockShared(Arg1, Arg2, a3, a4);
    }
    result = KeAbPostRelease(local_rbx, Arg2, a3, a4);
    result = KeLeaveGuardedRegion(local_rbx, Arg2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DEED6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DEED6[BB_006DEED6]
  bb_006DEEE2[BB_006DEEE2]
  bb_006DEEEA[BB_006DEEEA]
  bb_006DEED6 -->|branch| bb_006DEEEA
  bb_006DEED6 -->|fallthrough| bb_006DEEE2
  bb_006DEEE2 -->|flow| bb_006DEEEA
```
