# sub_00B369FE

- RVA: `0x00B369FE`–`0x00B36A1D` (길이 `31` bytes)
- VA: `0x0000000140B369FE`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A8E6C`
- 디코드: `7`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B36A01` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00B36A09` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00B36A0E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00B36A01` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00B36A09` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00B36A0E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B36A18` → [SmProcessCompressionInfoRequest + 0x2DB](../A0/SmProcessCompressionInfoRequest_function_00A0E980.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B369FE  48 8B CF                        mov rcx, rdi
00B36A01  E8 CA F3 72 FF                  call 0x140265dd0
00B36A06  48 8B CF                        mov rcx, rdi
00B36A09  E8 F2 AB 7A FF                  call 0x1402e1600
00B36A0E  E8 9D 6E 72 FF                  call 0x14025d8b0
00B36A13  BB A9 01 00 C0                  mov ebx, 0xc00001a9
00B36A18  E9 3E 82 ED FF                  jmp 0x140a0ec5b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B369FE(void)
{
    __int64 result;

    result = ExfTryToWakePushLock(v_rdi, a2, a3, a4);
    result = KeAbPostRelease(v_rdi, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_rdi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B369FE(void)
{
    int64_t result;

    result = ExfTryToWakePushLock(local_rdi, a2, a3, a4);
    result = KeAbPostRelease(local_rdi, a2, a3, a4);
    result = KeLeaveCriticalRegion(local_rdi, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B369FE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B369FE[BB_00B369FE]
```
