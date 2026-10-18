# PpmApplyIdlePolicy

- RVA: `0x004474A8`–`0x0044750A` (길이 `98` bytes)
- VA: `0x00000001404474A8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `20`개 명령, `98/98` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004474F8` → [PpmConvertTimeFrom](PpmConvertTimeFrom_function_00447510.md) (function, `0x00447510`)

### Direct callers
- [PpmResetIdlePolicy](PpmResetIdlePolicy_function_00447468.md) at `0x0044747E`

### Static image references
- `0x004474AC` → RVA `0x00E08380` (`.data`; read)
- `0x004474B3` → RVA `0x00F0CE0C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004474A8  48 83 EC 28                     sub rsp, 0x28
004474AC  4C 8B 0D CD 0E 9C 00            mov r9, qword ptr [rip + 0x9c0ecd]
004474B3  48 63 05 52 59 AC 00            movsxd rax, dword ptr [rip + 0xac5952]
004474BA  4C 8B 19                        mov r11, qword ptr [rcx]
004474BD  4C 69 C0 E8 01 00 00            imul r8, rax, 0x1e8
004474C4  43 8A 84 08 CC 00 00 00         mov al, byte ptr [r8 + r9 + 0xcc]
004474CC  88 41 48                        mov byte ptr [rcx + 0x48], al
004474CF  43 8A 94 08 D4 00 00 00         mov dl, byte ptr [r8 + r9 + 0xd4]
004474D7  88 51 47                        mov byte ptr [rcx + 0x47], dl
004474DA  43 8A 84 08 D5 00 00 00         mov al, byte ptr [r8 + r9 + 0xd5]
004474E2  88 51 45                        mov byte ptr [rcx + 0x45], dl
004474E5  BA 40 42 0F 00                  mov edx, 0xf4240
004474EA  88 41 46                        mov byte ptr [rcx + 0x46], al
004474ED  88 41 44                        mov byte ptr [rcx + 0x44], al
004474F0  43 8B 8C 08 D0 00 00 00         mov ecx, dword ptr [r8 + r9 + 0xd0]
004474F8  E8 13 00 00 00                  call 0x140447510
004474FD  41 89 83 C4 02 00 00            mov dword ptr [r11 + 0x2c4], eax
00447504  48 83 C4 28                     add rsp, 0x28
00447508  C3                              ret
00447509  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmApplyIdlePolicy(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = (a3) * ((int)(*(unsigned int *)(v_rip + 11295058)));
    *(unsigned __int8 *)(a1 + 72) = (unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rip + 10227405) * 1 + 204));
    *(unsigned __int8 *)(a1 + 71) = (unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rip + 10227405) * 1 + 212));
    *(unsigned __int8 *)(a1 + 69) = (unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rip + 10227405) * 1 + 212));
    *(unsigned __int8 *)(a1 + 70) = (unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rip + 10227405) * 1 + 213));
    *(unsigned __int8 *)(a1 + 68) = (unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(v_rip + 10227405) * 1 + 213));
    result = PpmConvertTimeFrom((unsigned int)(*(unsigned int *)(a3 + *(unsigned __int64 *)(v_rip + 10227405) * 1 + 208)), (unsigned int)(0xF4240ULL), a3, *(unsigned __int64 *)(v_rip + 10227405));
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 708) = (unsigned int)(result);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmApplyIdlePolicy(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    a3 = (a3) * ((int32_t)(*(uint32_t *)(v_rip + 0xAC5952)));
    *(uint8_t *)(arg1 + 0x48) = (uint8_t)(*(uint8_t *)(a3 + *(uint64_t *)(v_rip + 0x9C0ECD) * 1 + 0xCC));
    *(uint8_t *)(arg1 + 0x47) = (uint8_t)(*(uint8_t *)(a3 + *(uint64_t *)(v_rip + 0x9C0ECD) * 1 + 0xD4));
    *(uint8_t *)(arg1 + 0x45) = (uint8_t)(*(uint8_t *)(a3 + *(uint64_t *)(v_rip + 0x9C0ECD) * 1 + 0xD4));
    *(uint8_t *)(arg1 + 0x46) = (uint8_t)(*(uint8_t *)(a3 + *(uint64_t *)(v_rip + 0x9C0ECD) * 1 + 0xD5));
    *(uint8_t *)(arg1 + 0x44) = (uint8_t)(*(uint8_t *)(a3 + *(uint64_t *)(v_rip + 0x9C0ECD) * 1 + 0xD5));
    result = PpmConvertTimeFrom((uint32_t)(*(uint32_t *)(a3 + *(uint64_t *)(v_rip + 0x9C0ECD) * 1 + 0xD0)), (uint32_t)(0xF4240ULL), a3, *(uint64_t *)(v_rip + 0x9C0ECD));
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x2C4) = (uint32_t)(result);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x44` | `8` | `W` |
| `Arg1` | `+ 0x45` | `8` | `W` |
| `Arg1` | `+ 0x46` | `8` | `W` |
| `Arg1` | `+ 0x47` | `8` | `W` |
| `Arg1` | `+ 0x48` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004474A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004474A8[BB_004474A8]
  bb_00447509[BB_00447509]
```
