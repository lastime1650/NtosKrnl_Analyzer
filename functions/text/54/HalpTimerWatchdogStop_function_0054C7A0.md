# HalpTimerWatchdogStop

- RVA: `0x0054C7A0`–`0x0054C7EB` (길이 `75` bytes)
- VA: `0x000000014054C7A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0054C7C2` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0054C7D1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0054C7A4` → RVA `0x00FC4028` (`.data`; read)
- `0x0054C7B0` → RVA `0x00FC2180` (`.data`; read/write)
- `0x0054C7B6` → RVA `0x00FC2184` (`.data`; read)
- `0x0054C7D6` → RVA `0x00FC2190` (`.data`; read/write)
- `0x0054C7DE` → RVA `0x00FC2184` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054C7A0  48 83 EC 28                     sub rsp, 0x28
0054C7A4  48 8B 15 7D 78 A7 00            mov rdx, qword ptr [rip + 0xa7787d]
0054C7AB  48 85 D2                        test rdx, rdx
0054C7AE  74 35                           je 0x14054c7e5
0054C7B0  FF 05 CA 59 A7 00               inc dword ptr [rip + 0xa759ca]
0054C7B6  80 3D C7 59 A7 00 00            cmp byte ptr [rip + 0xa759c7], 0
0054C7BD  74 26                           je 0x14054c7e5
0054C7BF  48 8B CA                        mov rcx, rdx
0054C7C2  E8 39 CD CB FF                  call 0x140209500
0054C7C7  48 8B C8                        mov rcx, rax
0054C7CA  48 8B 82 88 00 00 00            mov rax, qword ptr [rdx + 0x88]
0054C7D1  E8 FA E2 16 00                  call 0x1406baad0
0054C7D6  48 83 25 B2 59 A7 00 00         and qword ptr [rip + 0xa759b2], 0
0054C7DE  C6 05 9F 59 A7 00 00            mov byte ptr [rip + 0xa7599f], 0
0054C7E5  48 83 C4 28                     add rsp, 0x28
0054C7E9  C3                              ret
0054C7EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTimerWatchdogStop(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 10975357) == 0) goto loc_0054C7E5;
    if ((*(unsigned __int8 *)(v_rip + 10967495)) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 10975357);
        result = HalpTimerGetInternalData(a1, *(unsigned __int64 *)(v_rip + 10975357), a3, a4);
        a1 = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10975357) + 136);
        result = guard_dispatch_icall(a1, *(unsigned __int64 *)(v_rip + 10975357), a3, a4);
        *(unsigned __int8 *)(v_rip + 10967455) = 0;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpTimerWatchdogStop(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0xA7787D) == 0) goto loc_0054C7E5;
    if ((*(uint8_t *)(v_rip + 0xA759C7)) != 0) {
        a1 = *(uint64_t *)(v_rip + 0xA7787D);
        result = HalpTimerGetInternalData(a1, *(uint64_t *)(v_rip + 0xA7787D), a3, a4);
        a1 = result;
        result = *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7787D) + 0x88);
        result = guard_dispatch_icall(a1, *(uint64_t *)(v_rip + 0xA7787D), a3, a4);
        *(uint8_t *)(v_rip + 0xA7599F) = 0;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054C7A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054C7A0[BB_0054C7A0]
  bb_0054C7B0[BB_0054C7B0]
  bb_0054C7BF[BB_0054C7BF]
  bb_0054C7E5[BB_0054C7E5]
  bb_0054C7EA[BB_0054C7EA]
  bb_0054C7A0 -->|branch| bb_0054C7E5
  bb_0054C7A0 -->|fallthrough| bb_0054C7B0
  bb_0054C7B0 -->|branch| bb_0054C7E5
  bb_0054C7B0 -->|fallthrough| bb_0054C7BF
  bb_0054C7BF -->|flow| bb_0054C7E5
```
