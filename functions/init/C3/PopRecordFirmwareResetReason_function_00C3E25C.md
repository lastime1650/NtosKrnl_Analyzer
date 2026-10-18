# PopRecordFirmwareResetReason

- RVA: `0x00C3E25C`–`0x00C3E2A4` (길이 `72` bytes)
- VA: `0x0000000140C3E25C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PoInitSystem](../C7/PoInitSystem_function_00C72358.md) at `0x00C72C44`

### Static image references
- `0x00C3E269` → RVA `0x00E67430` (`.data`; write)
- `0x00C3E27F` → RVA `0x00E67438` (`.data`; write)
- `0x00C3E28D` → RVA `0x00E67440` (`.data`; read)
- `0x00C3E29B` → RVA `0x00E67450` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C3E25C  48 8B 91 F0 00 00 00            mov rdx, qword ptr [rcx + 0xf0]
00C3E263  8A 82 70 0D 00 00               mov al, byte ptr [rdx + 0xd70]
00C3E269  88 05 C1 91 22 00               mov byte ptr [rip + 0x2291c1], al
00C3E26F  80 BA 70 0D 00 00 00            cmp byte ptr [rdx + 0xd70], 0
00C3E276  74 2A                           je 0x140c3e2a2
00C3E278  48 8B 82 78 0D 00 00            mov rax, qword ptr [rdx + 0xd78]
00C3E27F  48 89 05 B2 91 22 00            mov qword ptr [rip + 0x2291b2], rax
00C3E286  0F 10 82 80 0D 00 00            movups xmm0, xmmword ptr [rdx + 0xd80]
00C3E28D  0F 11 05 AC 91 22 00            movups xmmword ptr [rip + 0x2291ac], xmm0
00C3E294  0F 10 8A 90 0D 00 00            movups xmm1, xmmword ptr [rdx + 0xd90]
00C3E29B  0F 11 0D AE 91 22 00            movups xmmword ptr [rip + 0x2291ae], xmm1
00C3E2A2  C3                              ret
00C3E2A3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopRecordFirmwareResetReason(__int64 a1)
{
    __int64 result;

    *(unsigned __int8 *)(v_rip + 2265537) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 240) + 3440));
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 240) + 3440);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 240) + 3440)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3448);
        *(unsigned __int64 *)(v_rip + 2265522) = result;
        *(unsigned __int64 *)(v_rip + 2265516) = v_xmm0;
        *(unsigned __int64 *)(v_rip + 2265518) = v_xmm1;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopRecordFirmwareResetReason(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    *(uint8_t *)(v_rip + 0x2291C1) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xD70));
    result = *(uint8_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xD70);
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xD70)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xD78);
        *(uint64_t *)(v_rip + 0x2291B2) = result;
        *(uint64_t *)(v_rip + 0x2291AC) = v_xmm0;
        *(uint64_t *)(v_rip + 0x2291AE) = v_xmm1;
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C3E25C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C3E25C[BB_00C3E25C]
  bb_00C3E278[BB_00C3E278]
  bb_00C3E2A2[BB_00C3E2A2]
  bb_00C3E2A3[BB_00C3E2A3]
  bb_00C3E25C -->|branch| bb_00C3E2A2
  bb_00C3E25C -->|fallthrough| bb_00C3E278
  bb_00C3E278 -->|flow| bb_00C3E2A2
```
