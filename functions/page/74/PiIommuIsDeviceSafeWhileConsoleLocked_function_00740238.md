# PiIommuIsDeviceSafeWhileConsoleLocked

- RVA: `0x00740238`–`0x0074024E` (길이 `22` bytes)
- VA: `0x0000000140740238`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PiDmaGuardProcessUpdateConsoleLockStateAction](../73/PiDmaGuardProcessUpdateConsoleLockStateAction_function_0073BACC.md) at `0x0073BC47`
- [PipDmgEnforceEnumerationPolicy](../73/PipDmgEnforceEnumerationPolicy_function_0073BEB4.md) at `0x0073BEFE`
- [PipDmgEnforceEnumerationPolicy](../73/PipDmgEnforceEnumerationPolicy_function_0073BEB4.md) at `0x0073BF22`
- [PnpSurpriseFailUnsafeDmaDevices](../A9/PnpSurpriseFailUnsafeDmaDevices_function_00A95B90.md) at `0x00A95CA6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00740238  8A 41 10                        mov al, byte ptr [rcx + 0x10]
0074023B  A8 01                           test al, 1
0074023D  75 0B                           jne 0x14074024a
0074023F  A8 08                           test al, 8
00740241  75 07                           jne 0x14074024a
00740243  A8 24                           test al, 0x24
00740245  0F 94 C0                        sete al
00740248  C3                              ret
00740249  CC                              int3
0074024A  B0 01                           mov al, 1
0074024C  C3                              ret
0074024D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiIommuIsDeviceSafeWhileConsoleLocked(__int64 a1)
{
    __int64 result;

    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 16))) & (1)) != 0) goto loc_0074024A;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 16))) & (8)) != 0) goto loc_0074024A;
    result = ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 16))) & (36)) == 0) ? 1 : 0;
    return result;
loc_0074024A:
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t PiIommuIsDeviceSafeWhileConsoleLocked(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x10))) & (1)) != 0) goto loc_0074024A;
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x10))) & (8)) != 0) goto loc_0074024A;
    result = ((((uint8_t)(*(uint8_t *)(arg1 + 0x10))) & (36)) == 0) ? 1 : 0;
    return result;
loc_0074024A:
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00740238&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00740238[BB_00740238]
  bb_0074023F[BB_0074023F]
  bb_00740243[BB_00740243]
  bb_00740249[BB_00740249]
  bb_0074024A[BB_0074024A]
  bb_0074024D[BB_0074024D]
  bb_00740238 -->|branch| bb_0074024A
  bb_00740238 -->|fallthrough| bb_0074023F
  bb_0074023F -->|branch| bb_0074024A
  bb_0074023F -->|fallthrough| bb_00740243
  bb_00740249 -->|flow| bb_0074024A
```
