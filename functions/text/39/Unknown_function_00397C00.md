# sub_00397C00

- RVA: `0x00397C00`–`0x00397C33` (길이 `51` bytes)
- VA: `0x0000000140397C00`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008140C`
- 디코드: `13`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00397C21` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00397C2C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00397C17` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00397C12` → [sub_00397982 + 0x19E](Unknown_function_00397982.md) (`tail-transfer`)
  - `0x00397C1F` → [sub_00397B9E + 0x29](Unknown_function_00397B9E.md) (`tail-transfer`)
  - `0x00397C28` → [sub_00397B9E + 0x29](Unknown_function_00397B9E.md) (`tail-transfer`)
  - `0x00397C31` → [sub_00397B9E + 0x2B](Unknown_function_00397B9E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00397C00  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00397C08  8B BC 24 90 00 00 00            mov edi, dword ptr [rsp + 0x90]
00397C0F  48 89 10                        mov qword ptr [rax], rdx
00397C12  E9 09 FF FF FF                  jmp 0x140397b20
00397C17  8B 05 9B EE C2 00               mov eax, dword ptr [rip + 0xc2ee9b]
00397C1D  A8 40                           test al, 0x40
00397C1F  74 A6                           je 0x140397bc7
00397C21  E8 6A 78 F7 FF                  call 0x14030f490
00397C26  84 C0                           test al, al
00397C28  74 9D                           je 0x140397bc7
00397C2A  8B CD                           mov ecx, ebp
00397C2C  E8 2F 78 F7 FF                  call 0x14030f460
00397C31  EB 96                           jmp 0x140397bc9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00397C00(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, unsigned int a18)
{
    *(unsigned __int64 *)(a17) = a2;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00397C00(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, void *Arg17, uint32_t Arg18)
{
    uint8_t *arg17 = (uint8_t *)Arg17;

    *(uint64_t *)(arg17) = Arg2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg17` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00397C00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00397C00[BB_00397C00]
  bb_00397C17[BB_00397C17]
  bb_00397C21[BB_00397C21]
  bb_00397C2A[BB_00397C2A]
  bb_00397C17 -->|fallthrough| bb_00397C21
  bb_00397C21 -->|fallthrough| bb_00397C2A
```
